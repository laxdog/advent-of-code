#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def rotate_and_reverse(platform):
    return [list(row[::-1]) for row in zip(*platform)]

def move_rocks(platform):
    for row in platform:
        for i, char in reversed(list(enumerate(row))):
            if char == "O":
                target_position = find_target_position(row, i)
                row[i], row[target_position] = '.', 'O'
    return platform

def find_target_position(row, start_index):
    for i in range(start_index + 1, len(row)):
        if row[i] in "#O":
            return i - 1
    return len(row) - 1

def calculate_load(platform):
    load = 0
    for row_num, row in enumerate(reversed(platform), start=1):
        load += row.count("O") * row_num
    return load

platform = get_lines()

seen_platforms = []
cycle = []
MAX_CYCLES = 10**9

for cycle_count in range(1, MAX_CYCLES + 1):
    for _ in range(4):
        platform = move_rocks(rotate_and_reverse(platform))

    if platform in seen_platforms:
        loop_start_index = seen_platforms.index(platform)
        cycle = seen_platforms[loop_start_index:]
        remaining_cycles = MAX_CYCLES - cycle_count
        index_at_max_cycle = remaining_cycles % len(cycle)
        print(calculate_load(cycle[index_at_max_cycle]))
        break

    seen_platforms.append(platform)