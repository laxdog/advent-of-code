#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def go(file_type=None):
    count = 0
    count2 = 0
    for line in get_lines(file_type):
        first, second = line.split(',')
        f1, f2 = map(int, first.split('-'))
        s1, s2 = map(int, second.split('-'))
        if (f1 <= s1 and f2 >= s2) or (f1 >= s1 and f2 <= s2):
            count += 1
        if len(set(range(f1, f2 + 1)) & set(range(s1, s2 + 1))) != 0:
            count2 += 1
    print(count)
    print(count2)

go(1)
go()
