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

lines = get_lines()
grid = defaultdict(lambda: defaultdict(lambda: ' '))
max_x, max_y = 20, 16
min_x, min_y = -2, -3
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

def draw_map():
    # os.system('clear')
    # header = ''.join([str(x % 10) for x in range(min_x, max_x)])
    # print(f"   {header}")
    for y in range(min_y, max_y + 1):
        row = ''.join([grid[x][y] for x in range(min_x, max_x + 1)])
        print(f"{y:{' '}3} {row}")

def covered(x, y):
    for sx, sy, m in signals:
        mxy = abs(x-sx)+abs(y-sy)
        if mxy <= m and (x, y) not in beacons:
            # print("X:", x, "Y:", y, "M:", m, "Mxy:", mxy)
            return True
    return False


# count = 0
# for i in range(-10_000_000, 10_000_000):
#     if covered(i, 2_000_000):
#         count += 1
# print("Part 1:", count)

# for x in range(4_000_000 + 1):
#     print(f"{x} of 4000000")
#     for y in range(4_000_000 + 1):
#         if not covered(x, y):
#             print((x * 4_000_000) + y)

# # Get each point just outside the range of a signal
# to_check = set()
# for sx, sy, m in signals:
#     m += 1 # go beyond signal range
#     # if 0 > sx + m > 4_000_000 or 0 > sy + m > 4_000_000: continue
#     count = 0
#     for signal in range(m + 1):
#         # if signal % 1000 == 0: print(f"{signal} of {m+1}")
#         for sig in range(signal + 1):
#             count += 1
#             print(signal, sig, count)
#             # sx1, sy1 = sx + sig, sy + (signal - sig)
#             # sx2, sy2 = sx + sig, sy - (signal - sig)
#             # sx3, sy3 = sx - sig, sy + (signal - sig)
#             # sx4, sy4 = sx - sig, sy - (signal - sig)
#             sx1, sy1 = sx + sig - m, sy + sig
#             sx2, sy2 = sx + sig - m, sy - sig
#             sx3, sy3 = sx - sig + m, sy + sig
#             sx4, sy4 = sx - sig + m, sy - sig
#             if grid[sx1][sy1] == ' ':  grid[sx1][sy1] = 'a'
#             if grid[sx2][sy2] == ' ':  grid[sx2][sy2] = 'b'
#             if grid[sx3][sy3] == ' ':  grid[sx3][sy3] = 'c'
#             if grid[sx4][sy4] == ' ':  grid[sx4][sy4] = 'd'
#             # sx1, sy1 = sx + sig - m, sy + sig
#             # sx2, sy2 = sx + sig - m, sy - sig
#             # sx3, sy3 = sx - sig + m, sy + sig
#             # sx4, sy4 = sx - sig + m, sy - sig
# 
#             # if 0 < sx1 < 4_000_000 and 0 < sy1 < 4_000_000: to_check.add((sx1, sy1))
#             # if 0 < sx2 < 4_000_000 and 0 < sy2 < 4_000_000: to_check.add((sx2, sy2))
#             # if 0 < sx3 < 4_000_000 and 0 < sy3 < 4_000_000: to_check.add((sx3, sy3))
#             # if 0 < sx4 < 4_000_000 and 0 < sy4 < 4_000_000: to_check.add((sx4, sy4))

 # Get each point just outside the range of a signal
to_check = set()
count = 0
end = len(signals)
for sx, sy, m in signals:
    grid[sx][sy] = str(m)
    m += 1 # go beyond signal range
    # if 0 > sx + m > 4_000_000 or 0 > sy + m > 4_000_000: continue
    for sig in range(m + 1 + 1):
        # sx1, sy1 = sx + sig, sy + (signal - sig)
        # sx2, sy2 = sx + sig, sy - (signal - sig)
        # sx3, sy3 = sx - sig, sy + (signal - sig)
        # sx4, sy4 = sx - sig, sy - (signal - sig)
        sx1, sy1 = sx + sig - (m + 0), sy + sig
        sx2, sy2 = sx + sig - (m + 0), sy - sig
        sx3, sy3 = sx - sig + (m + 0), sy + sig
        sx4, sy4 = sx - sig + (m + 0), sy - sig
        if grid[sx1][sy1] == ' ':  grid[sx1][sy1] = str(sig)
        if grid[sx2][sy2] == ' ':  grid[sx2][sy2] = str(sig)
        if grid[sx3][sy3] == ' ':  grid[sx3][sy3] = str(sig)
        if grid[sx4][sy4] == ' ':  grid[sx4][sy4] = str(sig)
        # sx1, sy1 = sx + sig - m, sy + sig
        # sx2, sy2 = sx + sig - m, sy - sig
        # sx3, sy3 = sx - sig + m, sy + sig
        # sx4, sy4 = sx - sig + m, sy - sig

        # to_check.add((sx1, sy1))
        # to_check.add((sx2, sy2))
        # to_check.add((sx3, sy3))
        # to_check.add((sx4, sy4))

        if 0 < sx1 < 4_000_000 and 0 < sy1 < 4_000_000: to_check.add((sx1, sy1))
        if 0 < sx2 < 4_000_000 and 0 < sy2 < 4_000_000: to_check.add((sx2, sy2))
        if 0 < sx3 < 4_000_000 and 0 < sy3 < 4_000_000: to_check.add((sx3, sy3))
        if 0 < sx4 < 4_000_000 and 0 < sy4 < 4_000_000: to_check.add((sx4, sy4))


count = 0
end = len(to_check)
print("Start check")
for x, y in to_check:
    count += 1
    if count % 10000000 == 0: print(f"{count} of {end}")
    if not covered(x, y):
        print(x, y, (x * 4_000_000) + y)


# draw_map()

# count = 0
# for i in range(min_x, max_x + 1):
#     if grid[i][10] == '#': count += 1
# print(count)
