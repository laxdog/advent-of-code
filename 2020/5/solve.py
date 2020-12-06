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
        return [line.strip().split('x') for line in f.readlines() if line.strip()]

def bisect(low, high, keep):
    gap = (high + 1 - low)//2
    if keep in ['F', 'L']:
        return low, high - gap
    return low + gap, high

def find_pos(bspId):
    row = bspId[0:7]
    col = bspId[7:]
    rp = 127
    cp = 7
    rl = 0
    cl = 0
    for c in row:
        rl, rp = bisect(rl, rp, c)
    for c in col:
        cl, cp = bisect(cl, cp, c)
    return rp * 8 + cp

def go1():
    lines = get_lines(sys.argv[1])
    return sorted([find_pos(line[0]) for line in lines])

def go2():
    idList = go1()
    return([x for x in range(idList[-1]) if x not in idList])

print(go1()[-1])
print(go2()[-1])
