#!/usr/bin/env python3

from itertools import  product
from pprint import pprint as pp

def get_lines():
    return parse_file('input')
    return parse_file('sample1')

def parse_file(file):
    with open(file, 'r') as f:
        lines = [[int(x) for x in line.strip()] for line in f.readlines() if line.strip()]
    return(lines)


def get_neighbours(y, x, maxx, maxy):
    neighbours = []
    for y1, x1 in [x for x in product([-1, 1, 0], repeat=2)]:
        if (y1, x1) != (0, 0) and maxy > y+y1 >= 0 and maxx > x+x1 >=0:
            neighbours.append((y+y1, x+x1))
    return neighbours

def go():
    data = get_lines()
    maxx = len(data)
    maxy = len(data[0])
    def flash(y, x, octos, flashed):
        num_flash = 1
        
        for neigh in get_neighbours(y, x, maxx, maxy):
            data[neigh[0]][neigh[1]] += 1
            if neigh not in flashed and data[neigh[0]][neigh[1]] > 9:
                flashed.append(neigh)
                nf, flashed = flash(neigh[0], neigh[1], octos, flashed)
                num_flash += nf
        return num_flash, flashed



    num_flash = 0
    steps = 1000
    for step in range(steps):
        flashed = []
        this_cyc = 0
        for i in range(maxy):
            for j in range(maxx):
                data[i][j] += 1
        for i in range(maxy):
            for j in range(maxx):
                if data[i][j] > 9 and (i, j) not in flashed:
                    flashed.append((i,j))
                    nf, flashed = flash(i, j, data, flashed)
                    num_flash += nf
        for i in range(maxy):
            for j in range(maxx):
                if data[i][j] > 9:
                    data[i][j] = 0
                    this_cyc += 1
        if step == 99:
            print(f"Step: {step+1}, num_flash: {num_flash}")
            pp(data)
        if this_cyc == maxx * maxy:
            print(f"Step: {step+1}, num_flash: {num_flash}")
            pp(data)
            break


go()