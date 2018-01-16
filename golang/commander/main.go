package main

import (
	"os"

	"fmt"

	"github.com/mason-fish/public_projects/golang/githubTool"
	"github.com/urfave/cli"
)

const (
	accessTokenFlag = "access-token"
	userFlag        = "user"
)

func main() {
	cliApp := cli.NewApp()
	cliApp.Name = "commander"
	cliApp.Usage = "access to a bunch of cli tools"
	cliApp.Commands = []cli.Command{
		{
			Name:      "github",
			ShortName: "gh",
			Usage:     "initiate github operations",
			Flags: []cli.Flag{
				cli.StringFlag{
					Name:   accessTokenFlag,
					Usage:  "supplies a github access token for authentication (default uses env GITHUB_ACCESS_TOKEN)",
					EnvVar: "GITHUB_ACCESS_TOKEN",
				},
				cli.StringFlag{
					Name:   userFlag,
					Usage:  "provides the github account username (default uses env GITHUB_USER)",
					EnvVar: "GITHUB_USER",
				},
			},
			Subcommands: []cli.Command{
				{
					Name:      "repos",
					ShortName: "r",
					Usage:     "use repos api",
					Subcommands: []cli.Command{
						{
							Name:      "create",
							ShortName: "c",
							Usage:     "create a new repository in the credential owner's account",
							Action: func(c *cli.Context) error {
								fmt.Println("feature is not yet available")
								return nil
							},
						},
						{
							Name:      "list",
							ShortName: "l",
							Usage:     "list repositories associated with credential owner's account",
							Action: func(c *cli.Context) error {
								tool := ghtool.New(&ghtool.Config{
									AuthToken: c.GlobalString(accessTokenFlag),
								})
								return tool.PrintRepos()
							},
						},
					},
				},
				{
					Name:      "issues",
					ShortName: "i",
					Usage:     "use issues api",
					Subcommands: []cli.Command{
						{
							Name:      "create",
							ShortName: "c",
							Usage:     "create a new issue on a given repo",
							Action: func(c *cli.Context) error {
								tool := ghtool.New(&ghtool.Config{
									AuthToken: c.GlobalString(accessTokenFlag),
									User:      c.GlobalString(userFlag),
								})
								return tool.CreateIssue()
							},
						},
						{
							Name:      "list",
							ShortName: "l",
							Usage:     "list issues associated with credential owner's account",
							Action: func(c *cli.Context) error {
								tool := ghtool.New(&ghtool.Config{
									AuthToken: c.GlobalString(accessTokenFlag),
								})
								return tool.PrintOpenIssues()
							},
						},
					},
				},
			},
		},
	}

	cliApp.Run(os.Args)
}
