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

	"github.com/fatih/color"
	"github.com/google/go-github/github"
	"golang.org/x/crypto/ssh/terminal"
	oath2 "golang.org/x/oauth2"
)

type Tool struct {
	cl *github.Client
}

type Config struct {
	AuthToken string
	Name      string
}

func New(config *Config) *Tool {
	ctx := context.Background()
	ts := oath2.StaticTokenSource(
		&oath2.Token{AccessToken: config.AuthToken},
	)
	tc := oath2.NewClient(ctx, ts)

	return &Tool{
		cl: github.NewClient(tc),
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

func getVIMInput() string {
	file, err := os.Create("githubToolTemp")
	if err != nil {
		log.Fatal("Create: ", err)
	}
	fmt.Println(file.Name())
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
