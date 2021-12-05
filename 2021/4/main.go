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

func getInput() ([]int, [][5][5]int) {

	dat, err := os.ReadFile("input")
	check(err)

	sliceData := strings.Split(strings.TrimSpace(string(dat)), "\n")
	var win_nums []int
	var cards [][5][5]int

	for _, num := range strings.Split(sliceData[0], ",") {
		real_num, _ := strconv.Atoi(strings.TrimSpace(num))
		win_nums = append(win_nums, real_num)
	}
	row_cnt := 0
	var card [5][5]int
	for _, line := range sliceData[2:] {
		if len(line) <= 3 {
			fmt.Println(card)
			cards = append(cards, card)
			card = [5][5]int{}
			row_cnt = 0
		} else {
			var row [5]int
			line = strings.TrimSpace(line)
			line = strings.Replace(line, "  ", " ", -1)
			for i, num := range strings.Split(string(line), " ") {
				row[i], err = strconv.Atoi(strings.TrimSpace(num))
				check(err)
			}
			card[row_cnt] = row
			row_cnt++
		}
	}
	cards = append(cards, card)
	return win_nums, cards
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

func checkResults(card [5][5]int) bool {
	// for i, row := range card {
	// 	r_cnt := 0
	// 	for _, col := range row {
	// 		if col == -1 {
	// 			r_cnt++
	// 			if r_cnt == 5 {
	// 				fmt.Println("winner (row): ", card)
	// 				return true
	// 			}
	// 		}
	// 	}
	// }
	r_sum := 0
	c_sum := 0
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			r_sum += card[i][j]
			c_sum += card[j][i]
		}
		if r_sum == -5 {
			fmt.Println("winner (row): ", card)
			return true
		}
		if c_sum == -5 {
			fmt.Println("winner (col): ", card)
			return true
		}
	}
	return false
}

func calc_ans(card [5][5]int, win_num int) {
	total := 0
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			if card[i][j] > 0 {
				total += card[i][j]
			}
		}
	}
	fmt.Println(win_num)
	fmt.Println(total * win_num)
}

func main() {
	win_nums, cards := getInput()
	fmt.Println("Nums:", win_nums, "\nCards: ", len(cards))

	results := make([][5][5]int, len(cards))
	copy(results, cards)
	for _, win_num := range win_nums {
		for card_i, card := range cards {
			for row_i, row := range card {
				for col_i, col := range row {
					if col == win_num {
						// fmt.Println("match: ", win_num, "card: ", card_i, row)
						results[card_i][row_i][col_i] = -1
						if checkResults(results[card_i]) {
							calc_ans(results[card_i], win_num)
							return
						}
					}
				}
			}
		}
	}

}
