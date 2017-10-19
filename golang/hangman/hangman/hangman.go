package hangman

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// Game represents a game of hangman, it keeps track of all of the essential components of a game.
type Game struct {
	Secret       []rune
	Strikes      int
	StrikeMax    int
	Guesses      []rune
	Size         int
	Progress     []rune
	CorrectCount int
}

// Config sets the secret and maximum amount of strikes for a game
type Config struct {
	Secret    string
	StrikeMax string
}

// New instantiates a new game with the given config that defines the secret word and maximum strikes.
func New(c *Config) *Game {
	secret := []rune(c.Secret)
	size := len(secret)
	progress := make([]rune, size)
	strikeMax, err := strconv.Atoi(c.StrikeMax)
	if err != nil {
		fmt.Println("Please provide an integer for the maximum strike amount.")
		return nil
	}
	// Write defaults first
	return &Game{
		Secret:       secret,
		Strikes:      0,
		StrikeMax:    strikeMax,
		Guesses:      []rune{},
		Size:         size,
		Progress:     progress,
		CorrectCount: 0,
	}
}

func (g *Game) Play() (bool, error) {
	if err := g.renderAndPoll(); err != nil {
		return false, fmt.Errorf("renderAndPoll error: %v", err)
	}

	return g.checkEnd(), nil
}

// renders current state and polls for a new entry
func (g *Game) renderAndPoll() error {
	currentProgress := ""
	for _, c := range g.Progress {
		if c == 0 {
			currentProgress += "_"
		} else {
			currentProgress += string(c)
		}
	}
	fmt.Println(currentProgress)

	// read user input
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Enter guess: ")
	input, _ := reader.ReadString('\n')

	// validate user input
	if len(input) != 2 {
		fmt.Println("Please only enter one character.")
		return nil
	}
	// convert to rune
	guess := rune(input[0])
	// check rune cache to see if this has been guessed before
	for _, c := range g.Guesses {
		if c == guess {
			fmt.Println("This character has already been guessed!")
			return nil
		}
	}

	// check if guess has any matches and set them if so
	if !g.getAndSetMatches(guess) {
		// if there is no match, increment the strike
		g.Strikes++
	}
	// store guess in guess cache
	g.Guesses = append(g.Guesses, guess)

	return nil
}

// getAndSetMatches will look for and set matched runes, and return true or false
// depending on if it found one or zero matches
func (g *Game) getAndSetMatches(guess rune) (matchFound bool) {
	for i, c := range g.Secret {
		// we have found a match
		if c == guess {
			matchFound = true
			g.Progress[i] = c
			g.CorrectCount++
		}
	}
	return matchFound
}

func (g *Game) checkEnd() bool {
	if g.Strikes >= g.StrikeMax {
		fmt.Println("Max strikes hit, game over!")
		return true
	}
	if g.CorrectCount == g.Size {
		fmt.Println("You won, great job!")
		return true
	}
	return false
}
