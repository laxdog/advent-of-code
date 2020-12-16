#!/usr/bin/env python

import sys
from collections import defaultdict

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    if file_type == '0':
        return parse_file()
    return parse_file('input.txt')

def parse_file(file=None):
    if file:
        with open(file, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]

    lines = [int(num) for num in lines[0].split(',')]
    return lines

lines = get_lines(sys.argv[1])

def go1():
    nums = defaultdict(list)
    last = lines[-1]
    current = 0
    for turn, start in enumerate(lines):
        nums[start] = [turn + 1]
    print(nums)

    for i in range(len(nums), 30000000):
    # for i in range(len(nums), 2020):
        turn = i + 1
        if last not in nums.keys():
            current = 0
        elif len(nums[last]) == 1:
            current = 0
        else:
            current = nums[last][-1] - nums[last][-2]


        nums[current].append(turn)
        last = current
    return(current)

def main():
    print(go1())
    # print(go2())

if __name__ == "__main__":
    main()

