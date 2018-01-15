package main

import (
	"github.com/satori/go.uuid"
	"log"
	"strconv"
	"sync"
	"fmt"
	"net/http"
	"io/ioutil"
	"bytes"
	"encoding/json"
)

const (
	outputFile = "output.json"
	dataAmount = 30000
	concurrency = 8
)

// Entry holds basic data stored in an input file
type Entry struct {
	ID string
	Name string
	Detail string
}

type semaTool struct {
	sema chan bool
	errCh chan error
	out chan Entry
	wg sync.WaitGroup
	buff bytes.Buffer
}

func newTool() *semaTool {
	return &semaTool{
		sema: make(chan bool, concurrency),
		errCh: make(chan error, 1),
		out: make(chan Entry),
		wg: sync.WaitGroup{},
	}
}

func main() {
	input := generateData()
	tool := newTool()
	// prepare handler routing
	collectorWG := sync.WaitGroup{}
	collectorWG.Add(1)
	go func() {
		for {
			select {
			case err := <-tool.errCh:
				log.Fatal("errCh: ", err)
			case entry, ok := <-tool.out:
				if !ok {
					collectorWG.Done()
					return
				}
				bytes, err := json.Marshal(entry)
				if err != nil {
					log.Fatal("Marshal: ", err)
				}
				tool.buff.Write(bytes)
			}
		}
	}()
		// prepare launcher routing
	for i, v := range input {
		tool.sema <- true
		tool.wg.Add(1)
		go func(i int, v Entry) {
			defer func() {
				tool.wg.Done()
				<-tool.sema
			}()
			res, err := http.Get("http://localhost:8080/random")
			if err != nil {
				tool.errCh <- err
				return
			}

			result, err := ioutil.ReadAll(res.Body)
			defer res.Body.Close()

			v.Detail = strconv.Itoa(i) + "   " + string(result)
			tool.out <- v
		}(i,v)
	}

	tool.wg.Wait()
	close(tool.out)
	collectorWG.Wait()

	ioutil.WriteFile(outputFile, tool.buff.Bytes(), 0644)
	fmt.Println("done!")
}

func generateData() []Entry {
	entries := make([]Entry, dataAmount)
	for i := 0; i < dataAmount; i++ {
		id, err := uuid.NewV4()
		if err != nil {
			log.Fatal("NewV4: ", err)
		}

		entries[i] = Entry{
			ID: id.String(),
			Name: "fake name " + strconv.Itoa(i),
		}
	}

	return entries
}