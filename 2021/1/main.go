package main

import (
	"bufio"
	"fmt"
	"os"
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
	//fmt.Print(string(dat))

	sliceData := strings.Split(string(dat), "\n")

	//fmt.Println(sliceData)
	return sliceData
}

func getInputInt() []int {
	file, err := os.Open("input")
	check(err)
	defer file.Close()

	numbers := []int{}

	// Read every line from input and convert to an int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		n, _ := strconv.Atoi(scanner.Text())
		numbers = append(numbers, n)
	}

	return numbers
}

func main() {
	data := getInputInt()
	//fmt.Println(data)

	tmp := 9999999
	cnt := 0
	for _, i := range data {
		if i > tmp {
			cnt++
			fmt.Println(i, cnt)
		}
		tmp = i
	}

	tmp = 9999999
	i := 0
	cnt = 0
	for x, _ := range data {
		if x > 1 && x < 1999 {
			i = data[x-1] + data[x] + data[x+1]
			fmt.Println(data[x-1]+data[x]+data[x+1], cnt)
		}
		if i > tmp {
			cnt++
			fmt.Println(i, cnt)
		}
		tmp = i
	}

}
