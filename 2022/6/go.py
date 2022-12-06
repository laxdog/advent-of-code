#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    if file_type == 3: return parse_file('sample3')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()][0]

def go(file_type=None):
    line = get_lines(file_type)
    for size in [4, 14]:
        for count in range(len(line) - size):
            seen = set(line[count:count + size])
            if len(seen) == size:
                print(count + size)
                break

go()
