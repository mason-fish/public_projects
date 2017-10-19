package main

import (
	"fmt"
	"io/ioutil"
	"log"

	yaml "gopkg.in/yaml.v2"
)

// yamlDAO represents the contents of a yaml file
type yamlDAO struct {
	Feature featureName `yaml:"feature"`
}

type featureName struct {
	FeatureName map[string]featureDetail `yaml:"featureName"`
}

type featureDetail struct {
	FeatureCategory string   `yaml:"featureCategory"`
	DbKey           []string `yaml:"dbKey"`
	Test            string   `yaml:"test"`
}

func main() {
	// read file, return contents as byte slice
	yamlFile, err := ioutil.ReadFile("input.yaml")
	if err != nil {
		log.Fatalf("ReadFile: %v", err)
	}

	// create new empty struct, store address
	yamlDAO := &yamlDAO{}

	// unmarshall yaml into struct with corresponding tags
	err = yaml.Unmarshal(yamlFile, yamlDAO)
	if err != nil {
		log.Fatalf("Unmarshal: %v", err)
	}

	fmt.Printf("%+v\n", yamlDAO)
	fmt.Println(yamlDAO.Feature.FeatureName["interfaceClassification"].DbKey[1])
}
