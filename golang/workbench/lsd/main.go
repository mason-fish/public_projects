package main

import "fmt"

// creating a one to many relationship between Human and Cat

type Human struct {
	Name string
}

type Cat struct {
	Name string
	Owner Human
}

func main() {
	fmt.Println("hello world")

}
