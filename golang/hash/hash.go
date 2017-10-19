package main

import (
	"fmt"
	"strings"
)

const (
	tableSize = 256
)

type node struct {
	key   string
	value string
	next  *node
}

func makeHash(str string, size int) (hash int) {
	for _, char := range str {
		hash += int(char)
	}
	hash %= size
	return
}

func storeKeyValue(k string, v string, t *[tableSize]node) {
	hash := makeHash(k, tableSize)
	new := node{key: k, value: v, next: nil}

	if t[hash].key != "" {
		i := &t[hash]
		for ; i.next != nil; i = i.next {
		}
		i.next = &new
	} else {
		t[hash] = new
	}
}

func getValue(k string, t *[tableSize]node) (value string, err error) {
	hash := makeHash(k, tableSize)

	if strings.Compare(t[hash].key, k) != 0 {
		i := &t[hash]
		for ; i.next != nil; i = i.next {
			if strings.Compare(i.key, k) == 0 {
				return i.value, nil
			}
		}
		return "", fmt.Errorf("No match")
	}
	return t[hash].value, nil
}

func main() {
	var t [tableSize]node
	storeKeyValue("one", "Heyo 1!", &t)
	storeKeyValue("two", "Heyo 2!", &t)
	storeKeyValue("three", "Heyo 3!", &t)

	v, err := getValue("three", &t)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(v)

	v, err = getValue("one", &t)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(v)
	fmt.Printf("%+v", t)
}
