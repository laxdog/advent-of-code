#!/usr/bin/env python

import sys
from itertools import product
import operator

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def get_adj(x, y, max_x, max_y):
    if 0 < x < max_x:
        x1 = range(x - 1, x + 2)
    elif x == max_x:
        x1 = range(x - 1, x + 1)
    elif x == 0:
        x1 = range(x, x + 2)
    if 0 < y < max_y:
        y1 = range(y - 1, y + 2)
    if y == max_y:
        y1 = range(y - 1, y + 1)
    if y == 0:
        y1 = range(y, y + 2)
    lst = [p for p in product(x1, y1)]
    lst = [p for p in lst if p != (x, y)]
    return lst

def get_next_seat(cur_state, seat):
    col = seat[0]
    row = seat[1]
    adj = get_adj(col, row, max_x, max_y)
    if cur_state[row][col] == '.':
        return '.'
    occupied = 0
    for adj_seat in adj:
        adj_col = adj_seat[0]
        adj_row = adj_seat[1]
        occupied += cur_state[adj_row][adj_col] == '#'
    if occupied >= 4 and cur_state[row][col] == '#':
        return 'L'
    if occupied == 0 and cur_state[row][col] == 'L':
        return '#'
    return  cur_state[row][col]


def get_los(cur_state, x, y):
    if cur_state[y][x] == '.':
        return '.'
    moves = [x for x in product([-1, 1, 0], repeat=2) if x != (0, 0)]
    all_found = ""
    for move in moves:
        found = ""
        z = (x, y)
        while not found:
            z = tuple(map(operator.add, z, move))
            if 0 <= z[0] <= max_x and 0 <= z[1] <= max_y:
                loc = cur_state[z[1]][z[0]]
                if loc == ".":
                    continue
                else:
                    found = loc
            else:
                break
            all_found += found
    if all_found.count('#') >= 5 and cur_state[y][x] == '#':
        return 'L'
    if all_found.count('#') == 0 and cur_state[y][x] == 'L':
        return '#'
    return cur_state[y][x]



def go1():
    cur_state = lines[:]
    while True:
        next_state = []
        for y, row in enumerate(cur_state):
            next_state.append("")
            for x, _ in enumerate(row):
                next_state[y] += get_next_seat(cur_state, (x, y))


        if cur_state == next_state:
            return("".join(cur_state).count("#"))
        cur_state = next_state

def go2():
    cur_state = lines[:]
    while True:
        next_state = []
        for y, row in enumerate(cur_state):
            next_state.append("")
            for x, _ in enumerate(row):
                next_state[y] += get_los(cur_state, x, y)


        if cur_state == next_state:
            return("".join(cur_state).count("#"))
        cur_state = next_state

lines = get_lines(sys.argv[1])
max_y = len(lines) - 1
max_x = len(lines[0]) - 1

def main():
    print(go1())
    print(go2())

if __name__ == "__main__":
    main()

