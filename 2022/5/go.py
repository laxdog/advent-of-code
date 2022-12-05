#!/usr/bin/env python3

from copy import deepcopy

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

start = ""
for line in get_lines():
    if line.startswith('['):
        start += line + '                \n'

alls1 = []
for stack in range(9):
    alls1.append([])

for row in start.split('\n'):
    if row == '': break
    for char in range(1, 34, 4):
        if row[char] != ' ': alls1[char//4].append(row[char])

alls2 = deepcopy(alls1)

def go(file_type=None):
    for line in get_lines(file_type):
        if line.startswith('move'):
            num = int(line.split()[1])
            fromS = int(line.split()[3]) - 1
            toS = int(line.split()[5]) - 1
            for move in range(num):
                alls1[toS].insert(0, alls1[fromS].pop(0))
                alls2[toS].insert(0, alls2[fromS].pop(num - move - 1))

    print("".join([x[0] for x in alls1]))
    print("".join([x[0] for x in alls2]))

go()
# go()
