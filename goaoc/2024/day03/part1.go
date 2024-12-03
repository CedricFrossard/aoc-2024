package main

import (
	"fmt"
	"regexp"
	"strconv"
)

func doPartOne(input string) int {
	re := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
	var matches = re.FindAllStringSubmatch(input, -1)

	var result int

	for i, s := range matches {
		fmt.Println(i, s)
		a, _ := strconv.Atoi(s[1])
		b, _ := strconv.Atoi(s[2])
		result += a * b
	}
	return result
}
