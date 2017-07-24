package main

import "net/http"

// Route is a struct to hold parameter for each route
// such as name, http method, pattern (within the URL, I believe)
// and then which function is the proper handler for this route.
type Route struct {
	Name        string
	Method      string
	Pattern     string
	HandlerFunc http.HandlerFunc
}

// Routes is a slice of the Route struct
type Routes []Route

var routes = Routes{
	Route{
		"PostInfo",
		"POST",
		"/sendInfo",
		PostInfo,
	},
	Route{
		"Upload",
		"POST",
		"/uploadFile",
		upload,
	},
}
