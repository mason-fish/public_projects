package main

import (
	"fmt"
	"github.com/mason-fish/public_projects/golang/workbench/bstTools/tree"
)

func main() {
	root := tree.New()
	for i := 15; i > 0; i-- {
		root.Insert(i)
	}
	fmt.Println(root)
	fmt.Println(root.Len())
	fmt.Println(root.IsBST())
}