package example

import (
	"bytes"
)

// Comma inserts a comma every three bytes into a given string.
func Comma(s string) string {
	result := bytes.Buffer{}
	for i, c := range s {
		result.WriteRune(c)
		if (i+1)%3 == 0 {
			result.WriteString(",")
		}
	}
	return result.String()
}
