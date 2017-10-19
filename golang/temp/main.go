package main

import (
	"fmt"

	"time"

	"bytes"

	"github.com/mason-fish/study/golang/workbench"
)

//func main() {
//	var fileContents []byte
//	var err error
//	for {
//		fmt.Print("Please provide the name of a file to read: ")
//
//		// get file name from user input
//		var fileName string
//		fmt.Scanln(&fileName)
//
//		fileContents, err = ioutil.ReadFile(fileName)
//		if err != nil {
//			fmt.Printf("Could not read the filename given: %v\n", err)
//			continue
//		}
//		break
//	}
//
//	fmt.Print("Great, here is what is inside that file: ", fileContents)
//}

//func main() {
//	fmt.Println(example.Comma("Sup world"))
//}o

// test out workbench.ChannelExp()
func main() {
	urls := []string{
		"https://google.com",
		"https://yahoo.com",
		"http://www.mobiustrio.org",
		"https://store.docker.com",
		"https://google.com",
		"httzzzps://yahoo.com",
	}
	ch := make(chan string)
	go workbench.ChannelExp(urls, ch)

	buff := bytes.Buffer{}
	for range urls {
		buff.WriteString(fmt.Sprintln(<-ch))
	}

	fmt.Printf("DONE.\nRESULTS:\n%s", buff.String())
}

// run as gorouting, main will hav final word
func spinner(delay time.Duration) {
	for {
		for _, c := range `\|/-` {
			fmt.Printf("\r%c", c)
			time.Sleep(delay)
		}
	}
}

//func main() {
//	go spinner(time.Millisecond * 50)
//	time.Sleep(time.Second * 3)
//}
