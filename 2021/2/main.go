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

func getInput() ([]string, []int) {

	dat, err := os.ReadFile("input")
	check(err)
	//fmt.Print(string(dat))

	sliceData := strings.Split(string(dat), "\n")
	var dirs []string
	var vels []int

	for x, line := range sliceData {

		if x < 1000 {
			dirs = append(dirs, strings.Split(string(line), " ")[0])
			vel, _ := strconv.Atoi(strings.Split(string(line), " ")[1])
			vels = append(vels, vel)

		}
	}
	return dirs, vels
}

func main() {
	dirs, vels := getInput()
	fmt.Println(dirs, vels)

	x := 0
	y := 0
	for i, _ := range vels {
		if dirs[i] == "forward" {
			x += vels[i]
		}
		if dirs[i] == "down" {
			y += vels[i]
		}
		if dirs[i] == "up" {
			y -= vels[i]
		}
	}
	fmt.Println(x, y, x*y)

	x = 0
	y = 0
	a := 0
	for i, _ := range vels {
		if dirs[i] == "forward" {
			x += vels[i]
			y += vels[i] * a
		}
		if dirs[i] == "down" {
			a += vels[i]
		}
		if dirs[i] == "up" {
			a -= vels[i]
		}
	}
	fmt.Println(x, y, x*y)
}
