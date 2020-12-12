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
        lines = [line.strip() for line in f.readlines() if line.strip()]
        return [(x[0], int(x[1:])) for x in lines]


def go1():
    dirs = 'ESWN' * 100
    facing = 'E'
    x = y = 0
    for ins, val in lines:
        if ins == 'F':
            ins = facing
        if ins == 'E':
            x += val
        if ins == 'W':
            x -= val
        if ins == 'N':
            y += val
        if ins == 'S':
            y -= val
        if ins in ['R', 'L']:
            t = (val % 360)//90
            f = dirs.index(facing)
            if ins == 'L':
                facing = dirs[f - t]
            else:
                facing = dirs[t + f]

    return(abs(x) + abs(y))

# 31153 high
def go2():
    wp= (10, 1)
    ship = (0, 0)
    t = 0
    for ins, val in lines:
        if ins == 'F':
            for _ in range(val):
                ship = tuple(map(operator.add, ship, wp))
        if ins == 'E':
            wp = (wp[0] + val, wp[1])
        if ins == 'W':
            wp = (wp[0] - val, wp[1])
        if ins == 'N':
            wp = (wp[0], wp[1] + val)
        if ins == 'S':
            wp = (wp[0], wp[1] - val)
        if ins in ['R', 'L']:
            if ins == 'L' and val != 180:
                val += 180
            t = (val % 360)//90
            if t == 1:
                wp = (wp[1], wp[0] * - 1)
            if t == 2:
                wp = (wp[0] * - 1, wp[1] * - 1)
            if t == 3:
                wp = (wp[1] * - 1, wp[0])
        x, y = ship
        print((ins, val, t), ship, wp)
    return(abs(x) + abs(y))


lines = get_lines(sys.argv[1])

def main():
    print(go1())
    print(go2())

if __name__ == "__main__":
    main()

