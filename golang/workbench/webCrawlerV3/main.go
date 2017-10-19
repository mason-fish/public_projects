package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
	"strconv"
	"sync"

	"time"

	"github.com/mason-fish/study/golang/workbench/webCrawlerV3/links"
)

type buffLock struct {
	sync.Mutex
	buff bytes.Buffer
}

func (b *buffLock) write(url string) {
	b.Lock()
	b.buff.WriteString(url)
	b.Unlock()
}

type countLock struct {
	sync.Mutex
	count int
}

func (c *countLock) add(i int) {
	c.Lock()
	c.count += i
	c.Unlock()
}

func (c *countLock) get() int {
	c.Lock()
	defer c.Unlock()
	return c.count
}

type managerConfig struct {
	maxResult int
	threadCap int
	count     int
}

type manager struct {
	outC      chan string
	inC       chan []string
	maxResult int
	threadCap int
	count     *countLock
	buff      *buffLock
}

func newManager(config *managerConfig) *manager {
	outC := make(chan string)
	inC := make(chan []string)

	return &manager{
		outC:      outC,
		inC:       inC,
		maxResult: config.maxResult,
		threadCap: config.threadCap,
		buff:      &buffLock{},
		count:     &countLock{},
	}
}

func (m *manager) start() {
	var wg sync.WaitGroup
	var inWG sync.WaitGroup
	for i := 0; i < m.threadCap; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for url := range m.outC {
				m.buff.write(url)
				urls, err := links.Extract(url)
				if err != nil {
					log.Printf("Extract: %v", err)
				}

				inWG.Add(1)
				go func() {
					m.inC <- urls
					inWG.Done()
				}()
			}
		}()
	}

	count := 0
	seen := map[string]bool{}
	var finalWG sync.WaitGroup
	for urls := range m.inC {
		for _, url := range urls {
			// exit strategy
			if count > m.maxResult {
				close(m.outC)
				wg.Wait()
				// drain inC, discard values, to avoid goroutine leaks
				finalWG.Add(1)
				go func() {
					for _ = range m.inC {
					}
					finalWG.Done()
				}()
				inWG.Wait()
				close(m.inC)
				finalWG.Wait()
				return
			}
			if seen[url] {
				// dedupe (don't send to workers, just continue)
				continue
			}
			count++
			seen[url] = true
			m.outC <- url
		}
	}
}

func collectParams() (url string, maxResults, threadCap int) {
	if len(os.Args) != 4 {
		fmt.Println("Please provide an initial url, result amount, and concurrency capacity.")
		os.Exit(1)
	}
	url = os.Args[1]
	maxResults, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Println("result amount should be an integer")
		os.Exit(1)
	}

	threadCap, err = strconv.Atoi(os.Args[3])
	if err != nil {
		fmt.Println("concurrency capacity should be an integer")
		os.Exit(1)
	}

	return url, maxResults, threadCap
}

func main() {
	start := time.Now()
	go func() {
		for {
			for _, c := range `\|/-` {
				fmt.Printf("\r%c", c)
				time.Sleep(time.Millisecond * 50)
			}
		}
	}()

	url, maxResult, threadCap := collectParams()

	manager := newManager(&managerConfig{
		maxResult: maxResult,
		threadCap: threadCap,
	})

	go func() {
		manager.outC <- url
	}()
	// fire off crawler army
	manager.start()

	fmt.Println(manager.buff.buff.String())
	fmt.Printf("\nOperation took %.2f seconds\n", time.Since(start).Seconds())
}
