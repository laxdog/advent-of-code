#!/usr/bin/env python3

from copy import deepcopy

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

start = """[P]     [C]         [M]            
[D]     [P] [B]     [V] [S]        
[Q] [V] [R] [V]     [G] [B]        
[R] [W] [G] [J]     [T] [M]     [V]
[V] [Q] [Q] [F] [C] [N] [V]     [W]
[B] [Z] [Z] [H] [L] [P] [L] [J] [N]
[H] [D] [L] [D] [W] [R] [R] [P] [C]
[F] [L] [H] [R] [Z] [J] [J] [D] [D]"""


s1, s2, s3, s4, s5, s6, s7, s8, s9 = [], [], [], [], [], [], [], [], []
alls1 = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

for row in start.split('\n'):
    if row[1] != ' ': s1.append(row[1])
    if row[5] != ' ': s2.append(row[5])
    if row[9] != ' ': s3.append(row[9])
    if row[13] != ' ': s4.append(row[13])
    if row[17] != ' ': s5.append(row[17])
    if row[21] != ' ': s6.append(row[21])
    if row[25] != ' ': s7.append(row[25])
    if row[29] != ' ': s8.append(row[29])
    if row[33] != ' ': s9.append(row[33])

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

    out = ""
    for s in alls1:
        out += s[0]
    print(out)
    out = ""
    for s in alls2:
        out += s[0]
    print(out)

go()
# go()
