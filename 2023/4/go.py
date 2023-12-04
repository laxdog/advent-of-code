#!/usr/bin/env python3

from collections import defaultdict

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

p1 = 0
matches = []
for line in get_lines(None):
    win = [x for x in line.split(' | ')[0].strip().split(' ') if x not in ['', 'Card']][1:]
    our = [x for x in line.split(' | ')[1].strip().split(' ') if x not in ['', 'Card']][0:]
    match = len([x for x in win if x in our])
    matches.append(match)
    total = 2 ** (match - 1) if match > 0 else 0
    p1 += total
print(p1)

card_counts = defaultdict(lambda: 1)

i = 0
while i < len(matches):
    match_count = matches[i]
    card_count = card_counts[i]
    for j in range(1, match_count + 1):
        if i + j < len(matches):
            card_counts[i + j] += card_count
    i += 1

p2 = sum(card_counts.values())
print(p2)
