#!/usr/bin/env python3

from collections import defaultdict

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

lines = get_lines()
grid = [[char for char in line] for line in lines]
num_rows = len(grid)
num_cols = len(grid[0])

sum_adjacent_numbers = 0
adjacent_to_gears = defaultdict(list)

for row in range(num_rows):
    gears = set()
    current_number = 0
    has_part = False

    for col in range(len(grid[row]) + 1):
        if col < num_cols and grid[row][col].isdigit():
            current_number = current_number * 10 + int(grid[row][col])
            for delta_row in [-1, 0, 1]:
                for delta_col in [-1, 0, 1]:
                    if 0 <= row + delta_row < num_rows and 0 <= col + delta_col < num_cols:
                        neighbor_char = grid[row + delta_row][col + delta_col]
                        if not neighbor_char.isdigit() and neighbor_char != '.':
                            has_part = True
                        if neighbor_char == '*':
                            gears.add((row + delta_row, col + delta_col))
        elif current_number > 0:
            for gear in gears:
                adjacent_to_gears[gear].append(current_number)
            if has_part:
                sum_adjacent_numbers += current_number
            current_number = 0
            has_part = False
            gears = set()

print(sum_adjacent_numbers)

# Part 2
product_of_pairs = 0
for position, numbers in adjacent_to_gears.items():
    if len(numbers) == 2:
        product_of_pairs += numbers[0] * numbers[1]

print(product_of_pairs)
