#!/usr/bin/env python3

import sys

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split(' -> ') for line in f.readlines() if line.strip()]

def go(part=1):
    lines = get_lines()
    rows, cols = (1000, 1000)
    output = [[0 for _ in range(cols)] for _ in range(rows)]
    for line in lines:
        x0, y0 = line
        x1, y1 = [int(i) for i in x0.split(',')]
        x2, y2 = [int(i) for i in y0.split(',')]
        dx = -1 if x1 > x2 else 1
        dy = -1 if y1 > y2 else 1
        if x1 == x2 or y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    output[x][y] += 1
        elif part==2:
            for i in range(abs(x1 -  x2) + 1):
                output[x1+i*dx][y1+i*dy] += 1

    count = 0
    for row in range(rows):
        for col in range(cols):
            if output[col][row] > 1:
                count += 1
    print("Count", count)
    return(output)

go()
go(part=2)
