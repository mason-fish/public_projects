package actions

import (
	"fmt"

	"net/http"

	"strings"

	"sort"

	"github.com/urfave/cli"
	"golang.org/x/net/html"
)

var omittedTags = []string{"script", "style"}

func GetKeyWords(ctx *cli.Context) error {
	url := ctx.Args().Get(0)
	if url == "" {
		return fmt.Errorf("no url provided")
	}

	res, err := http.Get(url)
	if err != nil {
		return fmt.Errorf("failed to get url: %v", err)
	}
	defer res.Body.Close()

	dom, err := html.Parse(res.Body)
	if err != nil {
		return fmt.Errorf("failed to parse html: %v", err)
	}

	txtTags := getTextTags(dom)

	words := []string{}
	for _, txt := range txtTags {
		words = append(words, toWords(txt)...)
	}

	dict := map[string]int{}
	for _, val := range words {
		dict[val]++
	}

	sorted := sortKeywords(dict)
	fmt.Println(sorted)

	return nil
}

type KeywordList []Keyword

type Keyword struct {
	Key   string
	Value int
}

func (k KeywordList) Less(i, j int) bool { return k[i].Value > k[j].Value }
func (k KeywordList) Len() int           { return len(k) }
func (k KeywordList) Swap(i, j int)      { k[i], k[j] = k[j], k[i] }
func (k KeywordList) String() string {
	format := "|%5v|%25s|%5v|\n"
	str := fmt.Sprintf(format, "RANK", "KEYWORD", "COUNT")
	for i, v := range k {
		str += fmt.Sprintf(format, i+1, v.Key, v.Value)
	}
	return str
}

func sortKeywords(list map[string]int) KeywordList {
	keywords := make(KeywordList, len(list))
	i := 0
	for k, v := range list {
		keywords[i] = Keyword{
			Value: v,
			Key:   k,
		}
		i++
	}
	sort.Sort(keywords)
	return keywords
}

func getTextTags(node *html.Node) []string {
	if node == nil {
		return nil
	}

	return doGetTextTags(node, []string{})
}

func doGetTextTags(node *html.Node, results []string) []string {
	for _, val := range omittedTags {
		if node.Type == html.ElementNode && node.Data == val {
			return results
		}
	}
	if data := strings.TrimSpace(node.Data); node.Type == html.TextNode && data != "" {
		return append(results, data)
	}

	for n := node.FirstChild; n != nil; n = n.NextSibling {
		results = doGetTextTags(n, results)
	}

	return results
}

func toWords(str string) []string {
	return strings.Split(str, " ")
}
