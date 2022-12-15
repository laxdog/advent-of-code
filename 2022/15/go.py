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

def draw_map():
    # os.system('clear')
    header = ''.join([str(x % 10) for x in range(min_x, max_x)])
    print(f"   {header}")
    for y in range(min_y, max_y + 1):
        row = ''.join([grid[x][y] for x in range(min_x, max_x + 1)])
        print(f"{y:{' '}3} {row}")

lines = get_lines()
grid = defaultdict(lambda: defaultdict(lambda: ' '))
max_x, max_y = 0, 0
min_x, min_y = math.inf, math.inf
signals = set()
beacons = set()
for line in lines:
    parse = line.replace(',', ' ').replace(':', ' ').replace('=', ' ').split()
    sx, sy = [int(c) for c in (parse[3], parse[5])]
    bx, by = [int(c) for c in (parse[-3], parse[-1])]
    m = abs(sx - bx) + abs(sy - by)
    print(f"Sensor: {sx, sy}, beacon: {bx, by}, manhattan: {m}")
    signals.add((sx, sy, m))
    beacons.add((bx, by))

def covered(x, y):
    for sx, sy, m in signals:
        mxy = abs(x-sx)+abs(y-sy)
        if mxy <= m and (x, y) not in beacons:
            # print("X:", x, "Y:", y, "M:", m, "Mxy:", mxy)
            return True
    return False


print(covered(0, 10))
count = 0
for i in range(-10_000_000, 10_000_000):
    if covered(i, 2_000_000):
        count += 1

print(count)
    # grid[sx][sy] = 'S'
    # grid[bx][by] = 'B'
    # for signal in range(m1):
    #     if signal % 1000 == 0:
    #         print(f"{signal} of {m1}")
    #     for sig in range(signal + 1):
    #         sx1, sy1 = sx + sig, sy + (signal - sig)
    #         sx2, sy2 = sx + sig, sy - (signal - sig)
    #         sx3, sy3 = sx - sig, sy + (signal - sig)
    #         sx4, sy4 = sx - sig, sy - (signal - sig)

    #         if grid[sx1][sy1] == ' ':  grid[sx1][sy1] = '#'
    #         if grid[sx2][sy2] == ' ':  grid[sx2][sy2] = '#'
    #         if grid[sx3][sy3] == ' ':  grid[sx3][sy3] = '#'
    #         if grid[sx4][sy4] == ' ':  grid[sx4][sy4] = '#'

# draw_map()
# count = 0
# for i in range(min_x, max_x + 1):
#     if grid[i][10] == '#': count += 1
# print(count)
