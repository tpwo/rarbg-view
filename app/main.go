package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {

	fs := http.FileServer(http.Dir("static"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))

	http.HandleFunc("/", root)

	fmt.Println("Listening...")
	http.ListenAndServe(":8000", nil)
}

func root(w http.ResponseWriter, req *http.Request) {
	w.Write(returnFile("static/index.html"))
}

func returnFile(path string) []byte {
	fileBytes, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}
	return fileBytes
}
