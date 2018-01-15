package tree

import (
	"strconv"
)

// Node represents the node fo a tree
type Node struct {
	Value int
	Left  *Node
	Right *Node
}

type Tree struct {
	Root  *Node
	Count int
}

func New() *Tree {
	return &Tree{}
}

func (t *Tree) Insert(val int) {
	t.Count++
	if t.Root == nil {
		t.Root = &Node{
			Value: val,
		}
		return
	}

	insert(val, t.Root)
}

func insert(val int, node *Node) {
	// this can be refactored to check base case first (node == nil)
	// and then add node, otherwise recurse.
	if val >= node.Value {
		if node.Right != nil {
			insert(val, node.Right)
			return
		} else {
			node.Right = &Node{
				Value: val,
			}
			return
		}
	} else {
		if node.Left != nil {
			insert(val, node.Left)
			return
		} else {
			node.Left = &Node{
				Value: val,
			}
			return
		}
	}
}

func (t *Tree) IsBST() bool {
	contents := collectNodes(t.Root, []int{})
	for i := 0; i < len(contents)-1; i++ {
		if contents[i] > contents[i+1] {
			return false
		}
	}
	return true
}

func (t *Tree) String() string {
	res := collectNodes(t.Root, []int{})
	resStr := ""
	for i, v := range res {
		resStr += strconv.Itoa(v)
		if i != len(res)-1 {
			resStr += " "
		}
	}
	return resStr
}

func (t *Tree) Len() int {
	return t.Count
}

func collectNodes(n *Node, results []int) []int {
	if n.Left != nil {
		results = append(results, collectNodes(n.Left, results)...)
	}
	results = append(results, n.Value)
	if n.Right != nil {
		results = append(results, collectNodes(n.Right, results)...)
	}

	return results
}
