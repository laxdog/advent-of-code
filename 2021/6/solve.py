#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input')
    return parse_file('sample1')

def parse_file(file):
    with open(file, 'r') as f:
        return [int(x) for  x in [line.strip().split(',') for line in f.readlines() if line.strip()][0]]

def go(days=80):
    fish_map = [0]*9
    for fish in get_lines():
        fish_map[fish] += 1
    for _ in range(days):
        day_pop = [0]*9
        for i, fish in enumerate(fish_map):
            if i == 0:
                day_pop[6] += fish
                day_pop[8] += fish
            else:
                day_pop[i-1] += fish
        fish_map = day_pop
    return fish_map
            


print(sum(go()))
print(sum(go(256)))
