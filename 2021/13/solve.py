#!/usr/bin/env python3

import pandas as pd
from collections import defaultdict
from pprint import pprint as pp

def get_lines(file='input'):
    coords = []
    folds = []
    with open(file, 'r') as f:
        for line in f.readlines():
                if line.strip() and '=' not in line:
                    coords.append([int(x) for x in line.strip().split(',')])
                elif line.strip() and '=' in line:
                    folds.append(line.strip().split(' ')[-1])
    return(coords, folds)


def go():
    coords, folds = get_lines()
    maxx = 0
    maxy = 0
    for x, y in coords:
        maxx = x if x > maxx else maxx
        maxy = y if y > maxy else maxy
    paper = [[" " for x in range(maxx + 1)] for y in range(maxy + 1)]
    for x, y in coords:
        paper[y][x] = '#'

    for fold in folds:
        dir, pos = fold.split('=')
        pos = int(pos)
        print(dir, pos, maxx, maxy, len(paper), len(paper[0]))

        flipped = False
        if dir == 'x':
            paper = pd.DataFrame(paper).T.values.tolist()
            dir = 'y'
            flipped = True
        if dir == 'y':
            folded = []
            for trow, brow in zip(paper[:pos], reversed(paper[pos+1:])):
                row = []
                for i, dot in enumerate(trow):
                    if dot == '#' or brow[i] == '#':
                        row.append('#')
                    else:
                        row.append(' ')
                folded.append(row)
        if flipped:
            folded = pd.DataFrame(folded).T.values.tolist()
            flipped = False
        paper = folded
        print(sum([x.count('#') for x in folded]))
    for row in folded:
        print("".join(row))

go()