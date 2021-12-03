package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getInputStr() []string {

	dat, err := os.ReadFile("input")
	check(err)

	sliceData := strings.Split(strings.TrimSpace(string(dat)), "\n")

	return sliceData
}

func getInputInt() []int {
	file, err := os.Open("input")
	check(err)
	defer file.Close()

	numbers := []int{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		n, err := strconv.Atoi(scanner.Text())
		check(err)
		numbers = append(numbers, n)
	}

	return numbers
}

func getInput() ([]string, []int) {

	dat, err := os.ReadFile("input")
	check(err)

	sliceData := strings.Split(strings.TrimSpace(string(dat)), "\n")
	var dirs []string
	var vels []int

	for _, line := range sliceData {
		dirs = append(dirs, strings.Split(string(line), " ")[0])
		vel, err := strconv.Atoi(strings.Split(string(line), " ")[1])
		check(err)
		vels = append(vels, vel)
	}
	return dirs, vels
}

func removeIndex(s []string, index int) []string {
	return append(s[:index], s[index+1:]...)
}

func removeDuplicateValues(intSlice []int) []int {
	keys := make(map[int]bool)
	list := []int{}

	for _, entry := range intSlice {
		if _, value := keys[entry]; !value {
			keys[entry] = true
			list = append(list, entry)
		}
	}
	return list
}

func main() {
	nums := getInputStr()

	first := ""
	second := ""

	for i := 0; i < 12; i++ {
		ones := 0
		zeroes := 0
		for _, num := range nums {
			if string(num[i]) == "1" {
				ones++
			}
			if string(num[i]) == "0" {
				zeroes++
			}
		}
		if ones < zeroes {
			first += "1"
			second += "0"
		} else {
			first += "0"
			second += "1"
		}
	}
	firstI, _ := strconv.ParseInt(first, 2, 64)
	secondI, _ := strconv.ParseInt(second, 2, 64)
	fmt.Println(first, second, firstI*secondI)

	tmpSlice := make([]string, len(nums))
	copy(tmpSlice, nums)

	for i := 0; i < 12; i++ {
		ones := 0
		zeroes := 0
		var indices []int
		for _, num := range tmpSlice {
			if string(num[i]) == "1" {
				ones++
			}
			if string(num[i]) == "0" {
				zeroes++
			}
		}
		if zeroes > ones {
			for j, num := range tmpSlice {
				if string(num[i]) == "1" {
					indices = append(indices, j)
				}
			}
		} else {
			for j, num := range tmpSlice {
				if string(num[i]) == "0" {
					indices = append(indices, j)
				}
			}
		}
		indices = removeDuplicateValues(indices)
		sort.Sort(sort.Reverse(sort.IntSlice(indices)))

		if len(tmpSlice) != 1 {
			for _, k := range indices {
				tmpSlice = removeIndex(tmpSlice, k)
			}
		}
	}
	first = tmpSlice[0]

	tmpSlice = make([]string, len(nums))
	copy(tmpSlice, nums)

	for i := 0; i < 12; i++ {
		ones := 0
		zeroes := 0
		var indices []int
		for _, num := range tmpSlice {
			if string(num[i]) == "1" {
				ones++
			}
			if string(num[i]) == "0" {
				zeroes++
			}
		}
		if zeroes > ones {
			for j, num := range tmpSlice {
				if string(num[i]) == "0" {
					indices = append(indices, j)
				}
			}
		} else {
			for j, num := range tmpSlice {
				if string(num[i]) == "1" {
					indices = append(indices, j)
				}
			}
		}
		indices = removeDuplicateValues(indices)
		sort.Sort(sort.Reverse(sort.IntSlice(indices)))

		if len(tmpSlice) != 1 {
			for _, k := range indices {
				tmpSlice = removeIndex(tmpSlice, k)
			}
		}
	}
	second = tmpSlice[0]

	firstI, _ = strconv.ParseInt(first, 2, 64)
	secondI, _ = strconv.ParseInt(second, 2, 64)
	fmt.Println(first, second, firstI*secondI)

}
