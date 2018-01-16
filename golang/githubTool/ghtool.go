package ghtool

import (
	"context"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"strings"

	"bufio"

	"github.com/fatih/color"
	"github.com/google/go-github/github"
	"golang.org/x/crypto/ssh/terminal"
	oath2 "golang.org/x/oauth2"
)

type Tool struct {
	cl     *github.Client
	config *Config
}

type Config struct {
	AuthToken string
	User      string
}

func New(config *Config) *Tool {
	ctx := context.Background()
	ts := oath2.StaticTokenSource(
		&oath2.Token{AccessToken: config.AuthToken},
	)
	tc := oath2.NewClient(ctx, ts)

	return &Tool{
		cl:     github.NewClient(tc),
		config: config,
	}
}

func (t *Tool) PrintRepos() error {
	repos, _, err := t.cl.Repositories.List(context.Background(), "", nil)
	if err != nil {
		return fmt.Errorf("Repositories.List: ", err)
	}

	// pretty print
	bytes, err := json.MarshalIndent(repos, "", "\t")
	if err != nil {
		return fmt.Errorf("MarshalIndent: ", err)
	}

	fmt.Println(string(bytes))

	return nil
}

func (t *Tool) PrintOpenIssues() error {
	issues, _, err := t.cl.Issues.List(context.Background(), true, &github.IssueListOptions{})
	if err != nil {
		return fmt.Errorf("Issues.List: ", err)
	}

	// TODO: should modify all of this print formatting into its own function using a buffer instead
	width, _, err := terminal.GetSize(0)
	if err != nil {
		return fmt.Errorf("GetSize: ", err)
	}
	heading := color.New(color.FgRed).Add(color.Underline)
	hr := color.New(color.FgHiBlue)
	for i, v := range issues {
		heading.Printf("Title:")
		fmt.Println("\t", *v.Title)
		heading.Printf("URL:")
		fmt.Println("\t", *v.URL)
		heading.Printf("Body:")
		fmt.Println("\t", *v.Body)
		if i < len(issues)-1 {
			hr.Println(strings.Repeat("-", width))
		}
	}

	return nil
}

func (t *Tool) CreateIssue() error {
	owner := getCLIInput("Enter repo owner")
	repo := getCLIInput("Enter repo name")
	title := getCLIInput("Enter issue name")
	body := getVIMInput()
	iss, _, err := t.cl.Issues.Create(context.Background(), owner, repo,
		&github.IssueRequest{
			Title:    &title,
			Body:     &body,
			Assignee: &t.config.User,
		})
	if err != nil {
		fmt.Println(err)
		return fmt.Errorf("Issues.Create: ", err)
	}
	fmt.Printf("Issue #%d created: %s\n", *iss.Number, *iss.HTMLURL)

	return nil
}

func getCLIInput(prompt string) string {
	r := bufio.NewReader(os.Stdin)
	fmt.Printf("%s: ", prompt)
	input, err := r.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}

	return strings.TrimSuffix(input, "\n")
}

func getVIMInput() string {
	file, err := os.Create("githubToolTemp")
	if err != nil {
		log.Fatal("Create: ", err)
	}
	defer os.Remove(file.Name())

	cmd := exec.Command("vim", file.Name())
	cmd.Stdin = os.Stdin
	cmd.Stderr = os.Stderr
	cmd.Stdout = os.Stdout

	err = cmd.Start()
	if err != nil {
		log.Fatal("Start ", err)
	}
	err = cmd.Wait()
	if err != nil {
		log.Fatal("Wait ", err)
	}
	contents, err := ioutil.ReadFile(file.Name())
	if err != nil {
		log.Fatal("ReadAll ", err)
	}
	return string(contents)
}
