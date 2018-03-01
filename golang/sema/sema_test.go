package sema

import (
	"fmt"
	"sync"
	"testing"
	"time"
)

type testOut struct {
	a int
}

type result struct {
	sync.Mutex
	total int
}

func (r *result) add(x int) {
	r.Lock()
	r.total += x
	r.Unlock()
}

func TestSema(t *testing.T) {
	testData := []testOut{{
		a: 4,
	}, {
		a: 5,
	}, {
		a: 6,
	}}
	testResult := &result{}
	testFinishCB := func(out *testOut) error {
		if out.a == 0 {
			return fmt.Errorf("fake error")
		}

		testResult.add(out.a)
		return nil
	}
	testFireCB := func(in *testOut) error {
		time.Sleep(time.Millisecond * time.Duration(in.a*100))
		if in.a == 6 {
			return fmt.Errorf("I'm a 6, eww.")
		}
		return nil
	}

	semaTool, err := New(&Config{
		Concurrency: 10,
		Data:        testData,
		FinishCB:    testFinishCB,
		FireCB:      testFireCB,
	})

}
