package main

import (
	"net/http"

	"github.com/gorilla/mux"
)

// NewRouter is a function the, using the Route struct above
// along with the Routes struct slice above, will create a new route
func NewRouter() *mux.Router {
	router := mux.NewRouter().StrictSlash(true)
	for _, route := range routes {
		var handler http.Handler
		handler = route.HandlerFunc
		handler = Logger(handler, route.Name)

		router.
			Methods(route.Method).
			Path(route.Pattern).
			Name(route.Name).
			Handler(handler)
	}

	return router
}
