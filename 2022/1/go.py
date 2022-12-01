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
        return [line.strip() for line in f.readlines()]

def go():
    lines = get_lines()
    elves = []
    count = 0
    for cal in lines:
        try:
            count += int(cal)
        except:
            elves.append(count)
            count = 0
    print(sorted(elves)[-1])
    print(sorted(elves)[-1] + sorted(elves)[-2] + sorted(elves)[-3]) 

go()
