#!/usr/bin/env python

import sys
from collections import deque
from itertools import combinations
import copy
from functools import lru_cache


def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        lines = sorted([int(line.strip()) for line in f.readlines() if line.strip()])
        return [0] + lines + [max(lines) + 3]


@lru_cache
def paths_to_end(index):
    if index == len(lines) - 1:
        return 1
    combos = 0
    for j in range(index+1, len(lines)):
        if lines[j] - lines[index] <= 3:
            combos += paths_to_end(j)
    return combos

lines = get_lines(sys.argv[1])

def main():
    print(paths_to_end(0))

if __name__ == "__main__":
    main()

