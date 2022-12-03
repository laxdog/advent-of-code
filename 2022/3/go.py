#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def go(file_type=None):
    total = 0
    for sack in get_lines(file_type):
        x = len(sack)/2
        f, s = sack[:x], sack[x:]
        common = (list(set(f) & set(s)))
        for item in common:
            total += priority(item)
    print(total)

    count, total = 0, 0
    sacks = []
    for sack in get_lines(file_type):
        count += 1
        sacks.append(sack)
        if count == 3:
            common = (list(set(sacks[0]) & set(sacks[1]) & set(sacks[2])))
            count = 0
            sacks = []
            for item in common:
                total += priority(item)
    print(total)

# go(1)
go()
