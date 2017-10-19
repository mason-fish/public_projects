package mainh

import (
	"fmt"
	"net/http"
)

// channelExp is an experiment to send synchronous and asyncronous events to the same channel
// proccessing of these events is done in the main file
func ChannelExp(urls []string, ch chan<- string) {
	for i, url := range urls {
		// every other url we will not actually get, just send to channel
		if i > 0 && i%2 == 0 {
			go func(url string) {
				ch <- fmt.Sprint("screened: ", url)
			}(url)
			continue
		}

		go func(url string) {
			res, err := http.Get(url)
			if err != nil {
				ch <- fmt.Sprintf("get: %v", err)
				return
			}
			ch <- fmt.Sprintf("%s %s", url, res.Status)
		}(url)
	}
}
