#!/usr/bin/env python3

import copy
from collections import defaultdict
from pprint import pprint as pp

def get_lines():
    return parse_file('input')
    return parse_file('sample1')

def parse_file(file):
    with open(file, 'r') as f:
        lines = [line.strip().split()[0] for line in f.readlines() if line.strip()]
        height_map = defaultdict(lambda: defaultdict(lambda:9))
        for i, line in enumerate(lines):
            for j, h in enumerate(list(line)):
                height_map[i + 1][j +1] = int(h)
    return(height_map)


def check_coord(y, x, hmap):
    p = hmap[y][x]
    low = True
    if p >= hmap[y-1][x]:
        low &= False
    if p >= hmap[y+1][x]:
        low &= False
    if p >= hmap[y][x-1]:
        low &= False
    if p >= hmap[y][x+1]:
        low &= False
    return low

def get_neighbours(y, x, hmap):
    p = hmap[y][x]
    neighbours = []
    if p < hmap[y-1][x]:
        neighbours.append((y-1, x))
    if p < hmap[y+1][x]:
        neighbours.append((y+1, x))
    if p < hmap[y][x-1]:
        neighbours.append((y, x-1))
    if p < hmap[y][x+1]:
        neighbours.append((y, x+1))
    return neighbours

def go():
    data = get_lines()
    lowest = []
    lowestyx = []
    iter_data = copy.deepcopy(data)
    for i, row in iter_data.items():
        for j, col in row.items():
            if check_coord(i, j, data):
                lowest.append(col)
                lowestyx.append((i, j))
    print(sum([x +1 for x in lowest]))

    def find_basin(y, x, hmap, seen):
        basin_size = 1
        
        for neigh in get_neighbours(y, x, hmap):
            if neigh not in seen:
                seen.add(neigh)
                if hmap[neigh[0]][neigh[1]] != 9:
                    basin_size += find_basin(neigh[0], neigh[1], hmap, seen)
        return basin_size



    size_list = []
    seen = set()
    for low in lowestyx:
        seen.add(low)
        size_list.append(find_basin(low[0], low[1], data, seen))
    size_list.sort()
    print(size_list[-1] * size_list[-2] * size_list[-3])


go()
