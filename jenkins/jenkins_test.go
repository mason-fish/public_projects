package jenkins

import (
	"testing"
)

func TestJenkins(t *testing.T) {
	testStr := "pipeline"
	prep := prependJenkins(testStr)
	if prep != "jenkins-"+testStr {
		t.Error("strings should match")
	}
}
