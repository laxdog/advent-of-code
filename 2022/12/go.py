#!/usr/bin/python3
import sys

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

lines = get_lines(1)

rows = []
start = (None, None)

for y, line in enumerate(lines):
    row = []
    for x, point in enumerate(line):
        if point == 'S':
            start = (x, y)
            row.append(0)
        elif point == 'E': row.append(27)
        else: row.append(ord(point) - ord('a') + 1)
    rows.append(row)

X = len(rows[0])
Y = len(rows)

def get_adj(x, y):
    adj = []
    if x > 0:     adj.append((x - 1, y))
    if x < X - 1: adj.append((x + 1, y))
    if y > 0:     adj.append((x, y - 1))
    if y < Y - 1: adj.append((x, y + 1))
    return adj

seen = set()

queue = []
queue.append((start, 1))
seen.add(start)

while len(queue) > 0:
    (x, y), move_num = queue.pop(0)
    height = rows[y][x]
    all_adj = get_adj(x, y)
    for adj in all_adj:
        if rows[adj[1]][adj[0]] == 27 and height == 26:
            print(move_num)
    for adj in all_adj:
        to = rows[adj[1]][adj[0]]
        if to - height <= 1 and adj not in seen:
            seen.add(adj)
            queue.append((adj, move_num + 1))


