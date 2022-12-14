#!/usr/bin/env python3

from collections import defaultdict
from copy import deepcopy
import math
import os

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def gen_map(part=1):
    max_x, max_y = 0, 0
    min_x, min_y = math.inf, math.inf
    grid = defaultdict(lambda: defaultdict(lambda: ' '))
    lines = get_lines(1)
    for line in lines:
        coords = line.split(" -> ")
        for i, coord in enumerate(coords):
            x, y = [int(c) for c in coord.split(',')]
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)
            try:
                to_x, to_y = [int(c) for c in coords[i +1].split(',')]
                for dy in range(min(y, to_y), max(y, to_y) + 1):
                    for dx in range(min(x, to_x), max(x, to_x) + 1):
                        grid[dx][dy] = '#'
            except IndexError:
                pass
            grid[x][y] = '#'
    if part == 1: return grid, min_x, min_y, max_x, max_y

    # Part 2
    min_x -= 150
    max_x += 150
    max_y += 2
    for i in range(min_x, max_x): grid[i][max_y] = '#'
    return grid, min_x, min_y, max_x, max_y

def draw_map():
    os.system('clear')
    for y in range(0, max_y + 1):
        print(''.join([grid[x][y] for x in range(min_x, max_x + 1)]))

sand = (500, 0)
moves = [(0, 1), (-1, 1), (1, 1)]
oob = False
unit = 0

for part in [2]:
    grid, min_x, min_y, max_x, max_y = gen_map(part=part)
    while True:
        grain = [sand[0], sand[1]]
        resting = False
        # draw_map()
        while (not oob and not resting):
            collision = 0
            top = False
            for move in moves:
                grain_to = (grain[0] + move[0], grain[1] + move[1])
                if grain_to[0] < min_x or grain[0] > max_x or grain[1] > max_y: oob = True
                elif grid[grain_to[0]][grain_to[1]] in ['#', 'o']:
                    collision += 1
                else:
                    grid[grain_to[0]][grain_to[1]] = 'o'
                    grid[grain[0]][grain[1]] = ' '
                    grain = grain_to[:]
                    break # Don't process more moves
                if collision == 3:
                    grid[grain[0]][grain[1]] = 'o'
                    unit += 1
                    resting = True
                    if (grain[0], grain[1]) == sand:
                        top = True
        if oob or top:
            break
    print(f"Final count: {unit}")
