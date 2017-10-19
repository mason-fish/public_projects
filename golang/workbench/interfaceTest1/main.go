package main

import (
	"fmt"
	"math/big"
	"golang.org/x/net/html/atom"
)

type prepender interface {
	prepend(s string) string
	concrete() []byte
}

type wordManipulator struct {
	prefix string `json:"prefix" type:"string"`
	suffix string `json:"suffix" type:"string"`
}

func (w *wordManipulator) prepend(s string) string {
	return fmt.Sprintf("%s%s\n", w.prefix, s)
}

func (w *wordManipulator) concrete() *wordManipulator {
	return &wordManipulator{
		prefix: w.prefix,
		suffix: w.suffix,
	}
}

func main() {
	var wordMan prepender
	wordMan = &wordManipulator{
		prefix: "pre",
		suffix: "post",
	}
	fmt.Println(wordMan.prepend("historic")
}
