package jenkins

import (
	"testing"
	"github.com/stretchr/testify/require"
)

func TestJenkins(t *testing.T) {
	testStr := "pipeline"
	prep := prependJenkins(testStr)
	require.Equal(t, prep, "jenkins-" +testStr)
}
