#!/usr/bin/python3
import sys
from collections import defaultdict

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def check_cycle(cycle, X):
    global tot
    global text
    t1 = cycle - 1
    row = (cycle - 1) // 40
    col = (cycle - 1) % 40
    text[row][col] = '#' if abs(X-(col)) <= 1 else ' '
    if cycle in [20, 60, 100, 140, 180, 220]:
        tot += (X * cycle)

cycle = 0
X = 1
tot = 0
text = [['*' for _ in range(40)] for _ in range(6)]

for cmd in get_lines():
    match cmd.split():
        case ['noop']:
            cycle += 1
            check_cycle(cycle, X)
        case ['addx', val]:
            cycle += 1
            check_cycle(cycle, X)
            cycle += 1
            check_cycle(cycle, X)
            X += int(val)

print(cycle, tot, X)
for row in range(6):
    print(''.join(text[row]))

