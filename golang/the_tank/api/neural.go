package main

import (
	"fmt"
	"log"
	"os/exec"

	"gopkg.in/gomail.v2"
)

// Transform calls a shell command, th, to transform an image
// and then mail it. It takes two parameters, style, and image.
func Transform(imagePath string) {
	cmd := exec.Command(
		"th",
		"neural_style.lua",
		"-style_image",
		store.Style,
		"-content_image",
		imagePath,
		"-gpu",
		"-1",
		"-image_size",
		"256",
		"-num_iterations",
		"50",
	)

	err := cmd.Start()
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Waiting for command to finish...")
	err = cmd.Wait()

	// Send email after command has run
	SendMail()
	if err != nil {
		log.Printf("Command finished with error: %v", err)
		return
	}
	log.Printf("Command successfuly finished")
	fmt.Println("Please check your inbox!")

}

// SendMail emails the result of the neural network shell command
func SendMail() {
	m := gomail.NewMessage()
	m.SetHeader("From", "mason.e.fish@gmail.com")
	m.SetHeader("To", store.Email)
	m.SetHeader("Subject", "Your Image")
	m.SetBody("text/html", "Find your transformed image attached below!")
	m.Attach("out.png")

	d := gomail.NewDialer("smtp.gmail.com", 587, "mason.e.fish", "fiReFly87@")

	// Send the email
	if err := d.DialAndSend(m); err != nil {
		panic(err)
	}
}
