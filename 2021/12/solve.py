#!/usr/bin/env python3

from collections import defaultdict
from pprint import pprint as pp

def get_lines():
    return parse_file('sample1')
    return parse_file('input')

def parse_file(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return(lines)


def get_neighbours(y, x, maxx, maxy):
    neighbours = []
    for y1, x1 in [x for x in product([-1, 1, 0], repeat=2)]:
        if (y1, x1) != (0, 0) and maxy > y+y1 >= 0 and maxx > x+x1 >=0:
            neighbours.append((y+y1, x+x1))
    return neighbours

def go():
    data = get_lines()
    paths = defaultdict(list)
    for path in data:
        paths[path.split('-')[0]].append(path.split('-')[1])
        paths[path.split('-')[1]].append(path.split('-')[0])

    num_paths = 0
    def find_path(loc, paths, tpath):
        tpath.append(loc)
        if loc == 'end':
            return tpath
        for dest in paths[loc]:
            print(f"Loc: {loc}, Dest: {dest}, TPath: {tpath}")
            if dest not in ['start']:
                if dest.islower() and dest not in tpath:
                    tpath = find_path(dest, paths, tpath)
                if dest.isupper():
                    tpath = find_path(dest, paths, tpath)
        return tpath


    # Look at first location accessible from current that is not the start
    # Is it the end? Return the current path list if so
    # Is it lower case? If it is, have we already visited a lower case on this path? Skip it if so
    # Go to the new location, repeat the above

    tpath = []
    find_path('start', paths, tpath)
    print(num_paths)
    pp(paths)

go()