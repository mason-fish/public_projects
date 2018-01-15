package main

import (
	"os"

	"github.com/mason-fish/public_projects/golang/githubTool"
	"github.com/urfave/cli"
)

const (
	reposFlag       = "repos"
	accessTokenFlag = "access-token"
	issuesFlag      = "issues"
)

func main() {
	cliApp := cli.NewApp()
	cliApp.Name = "commander"
	cliApp.Usage = "access to a bunch of cli tools"
	cliApp.Commands = []cli.Command{
		{
			Name:      "github",
			ShortName: "g",
			Usage:     "initiate github operations",
			Flags: []cli.Flag{
				cli.BoolFlag{
					Name:  reposFlag,
					Usage: "access account repos",
				},
				cli.BoolFlag{
					Name:  issuesFlag,
					Usage: "access account issues",
				},
				cli.StringFlag{
					Name:   accessTokenFlag,
					Usage:  "supplies a github access token for authentication (default uses env GITHUB_ACCESS_TOKEN)",
					EnvVar: "GITHUB_ACCESS_TOKEN",
				},
			},
			Action: func(c *cli.Context) error {
				tool := ghtool.New(&ghtool.Config{
					AuthToken: c.String(accessTokenFlag),
				})
				if c.Bool(reposFlag) {
					return tool.PrintRepos()
				}
				if c.Bool(issuesFlag) {
					return tool.PrintOpenIssues()
				}
				return nil
			},
		},
	}

	cliApp.Run(os.Args)
}
