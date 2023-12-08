#!/usr/bin/env python3

from collections import defaultdict, Counter, OrderedDict
import math

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split(' = ') for line in f.readlines()]


def lcm_of_list(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // math.gcd(lcm, numbers[i])
    return lcm

def go():
    f_insts = []
    for inst in get_lines()[0][0]:
        if inst == 'L': f_insts.append(0)
        if inst == 'R': f_insts.append(1)

    dir = {}
    for line in get_lines()[2:]:
        dir[line[0]] = (line[1].split(', ')[0].replace('(',''), line[1].split(', ')[1].replace(')',''))

    loc = 'AAA'
    steps = 0
    while loc != 'ZZZ':
        for i in f_insts:
            steps += 1
            loc = dir[loc][i]
    print(steps)


    a_locs = []
    for key in dir.keys():
        if key[2] == 'A':
            a_locs.append(key)
    ans = []
    for loc in a_locs:
        steps = 0
        while loc[2] != 'Z':
            for i in f_insts:
                steps += 1
                loc = dir[loc][i]
        ans.append(steps)

    print(lcm_of_list(ans))

go()