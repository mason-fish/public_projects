package main

import "github.com/Sirupsen/logrus"

func main() {
	logger := logrus.New()
	logger.Fatalf("shit I'm peacing out: %s", "and that's that")
	logger.Info("Hello log world!")
}
