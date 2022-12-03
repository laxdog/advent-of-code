#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def go(file_type=None):
    sum = 0
    for round in get_lines(file_type):
        x = int(len(round)/2)
        f, s = round[:x], round[x:]
        print(f, s)
        common = (list(set(f) & set(s)))
        for item in common:
            print(item)
            if item.islower():
                sum += ord(item) - ord('a') + 1
            else:
                sum += ord(item) - ord('A') + 27

    print(sum)

    sackC = 0
    sum = 0
    sacks = []
    for round in get_lines(file_type):
        sackC += 1
        sacks.append(round)
        if sackC == 3:
            common = (list(set(sacks[0]) & set(sacks[1]) & set(sacks[2])))
            print(common, sacks)
            sackC = 0
            sacks = []
            for item in common:
                if item.islower():
                    sum += ord(item) - ord('a') + 1
                else:
                    sum += ord(item) - ord('A') + 27

        print(sum)
go(1)
go()
