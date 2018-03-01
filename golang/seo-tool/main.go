package main

import (
	"log"
	"os"

	"github.com/mason-fish/public_projects/golang/seo-tool/actions"
	"github.com/urfave/cli"
)

func main() {
	app := cli.NewApp()
	app.Name = "seo-tool"
	app.Usage = "collection of seo related data inspection"
	app.Commands = []cli.Command{{
		Name:   "keywords",
		Usage:  "find top keywords in a domain",
		Action: actions.GetKeyWords,
	}}

	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}
