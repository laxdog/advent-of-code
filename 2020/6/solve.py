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
        lines = [line.strip() for line in f.readlines()]
        index = 0
        ans = [" "]
        for line in lines:
            if len(line) == 0:
                index += 1
                ans.append(" ")
            else:
                ans[index] += f" {line}"
        return ans

def go1():
    return sum([len(set(x.replace(' ', ''))) for x in lines])

def go2():
    groups = [x.split() for x in lines]
    count = 0
    for group in groups:
        intersect = set(group[0])
        for person in group:
            intersect = set(intersect).intersection(person)
        count += len(intersect)
    return(count)

lines = get_lines(sys.argv[1])


print(go1())
print(go2())
