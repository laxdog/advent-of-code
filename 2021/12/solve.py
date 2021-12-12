#!/usr/bin/env python3

from collections import defaultdict
from pprint import pprint as pp

def get_lines():
    return parse_file('input')
    return parse_file('sample1')

def parse_file(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return(lines)

def go():
    paths = defaultdict(list)
    for path in get_lines():
        paths[path.split('-')[0]].append(path.split('-')[1])
        paths[path.split('-')[1]].append(path.split('-')[0])

    def find_path(loc, tpath=set(), twice=False):
        if loc == 'end':
            return 1
        if loc.islower() and loc in tpath:
            if loc == 'start':
                return 0
            if twice:
                twice = False
            else:
                return 0
        tpath = tpath.union({loc})
        cnt = 0
        for dest in paths[loc]:
            cnt += find_path(dest, tpath, twice)
        return cnt

    print(find_path('start', twice=False))
    print(find_path('start', twice=True))

go()
