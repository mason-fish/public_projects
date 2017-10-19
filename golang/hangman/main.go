package main

import (
	"github.com/mason-fish/study/golang/hangman/hangman"
)

func main() {
	rules := &hangman.Config{
		Secret:    "Hello",
		StrikeMax: "3",
	}
	game := hangman.New(rules)
	g, err := game.Play()
	for {
		if g || err != nil {
			return
		}
		g, err = game.Play()
	}
}
