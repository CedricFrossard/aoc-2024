package main

import (
	"fmt"
	"regexp"
	"strconv"
)

func doPartTwo(input string) int {
	re := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)`)
	var matches = re.FindAllStringSubmatch(input, -1)

	var result int
	var ignore = false

	for i, s := range matches {
		if s[0] == "do()" {
			ignore = false
		}
		if s[0] == "don't()" {
			ignore = true
		}

		if ignore {
			continue
		}

		fmt.Println(i, s)
		a, _ := strconv.Atoi(s[1])
		b, _ := strconv.Atoi(s[2])
		result += a * b
	}
	return result
}
