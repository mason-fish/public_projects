package sema

import (
	"fmt"
	"reflect"
	"sync"
)

//type callback func(interface{}) error

//  Config is the configuration for a semaphore
type Config struct {
	Concurrency int
	FireCB      interface{}
	FinishCB    interface{}
	Data        interface{}
}

// Sema represents a semaphore wrapper
type Sema struct {
	wg          sync.WaitGroup
	concurrency int
	data        interface{}
	out         chan interface{}
	sema        chan struct{}
	err         chan error
	fireCB      interface{}
	finishCB    interface{}
}

// New returns a new semaphore wrapper
// TODO: allow for fast fail or error report style handling
func New(c *Config) (*Sema, error) {
	if c.Concurrency == 0 {
		return nil, fmt.Errorf("concurrency must be set to 1 or greater")
	}
	// might handle generics here
	if c.FireCB == nil {
		return nil, fmt.Errorf("no exec function provided")
	}
	if c.FinishCB == nil {
		return nil, fmt.Errorf("no handler function provided")
	}
	if c.Data == nil {
		return nil, fmt.Errorf("no data provided")
	}

	fire := reflect.TypeOf(c.FireCB)
	fire

	return &Sema{
		wg:          sync.WaitGroup{},
		concurrency: c.Concurrency,
		finishCB:    c.FinishCB,
		fireCB:      c.FireCB,
		data:        c.Data,
		out:         make(chan interface{}, c.Concurrency),
		sema:        make(chan struct{}, c.Concurrency),
		err:         make(chan error),
	}, nil
}

func (s *Sema) drain() {
	fmt.Println("draining...")
	for {
		select {
		case out, ok := <-s.out:
			if !ok {
				return
			}
			fmt.Printf("discarded %v\n", out)
		}
	}
}

func (s *Sema) Start() {
	wg := sync.WaitGroup{}
	wg.Add(1)

	// start collector
	go func() {
		defer func() {
			wg.Done()
			s.drain()
		}()

		for {
			select {
			case out, ok := <-s.out:
				// if !ok then the channel has been closed, otherwise keep draining
				if !ok {
					fmt.Println("out just closed")
					return
				}
				if err := s.finishCB(out); err != nil {
					s.err <- err
				}
			case <-s.err:
				fmt.Println("error hit, closing down system...")
				return
			}
		}
	}()

	// start launcher
	for _, val := range s.data {
		s.wg.Add(1)
		s.sema <- struct{}{}
		go func() {
			defer func() {
				s.wg.Done()
				<-s.sema
			}()

			if err := s.fireCB(val); err != nil {
				s.err <- err
			}
		}()
	}

	s.wg.Wait()
	close(s.out)
	wg.Wait()
	fmt.Println("finished")
}
