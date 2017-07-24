package main

import (
	"crypto/md5"
	"fmt"
	"html/template"
	"io"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

// Meta holds user information
type Meta struct {
	Email string
	Style string
}

var store Meta

// PostInfo will record the options selected by the user (email and style)
func PostInfo(w http.ResponseWriter, r *http.Request) {

	fmt.Println("method:", r.Method) //get request method
	if r.Method == "GET" {
		t, _ := template.ParseFiles("deepImages.html")
		t.Execute(w, nil)
	} else {
		r.ParseForm()
		// logic part of log in
		store.Email = (strings.Join(r.Form["Email"], ""))
		store.Style = (strings.Join(r.Form["Style"], ""))

		log.Println("Email:", store.Email)
		log.Println("Style:", store.Style)

		fmt.Println("Please now go back and select an image then press the blue upload button!")
	}
}

// upload does some cool shit
func upload(w http.ResponseWriter, r *http.Request) {
	fmt.Println("method:", r.Method)
	if r.Method == "GET" {
		crutime := time.Now().Unix()
		h := md5.New()
		io.WriteString(h, strconv.FormatInt(crutime, 10))
		token := fmt.Sprintf("%x", h.Sum(nil))

		t, _ := template.ParseFiles("upload.gtpl")
		t.Execute(w, token)
	} else {
		r.ParseMultipartForm(32 << 20)
		file, handler, err := r.FormFile("uploadfile")
		if err != nil {
			fmt.Println(err)
			return
		}
		defer file.Close()
		fmt.Fprintf(w, "%v", handler.Header)
		f, err := os.OpenFile("./db/"+handler.Filename, os.O_WRONLY|os.O_CREATE, 0666)
		if err != nil {
			fmt.Println(err)
			return
		}

		defer Transform("./db/" + handler.Filename)
		defer f.Close()
		io.Copy(f, file)
	}
}
