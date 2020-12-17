#!/usr/bin/env python

import sys
import cProfile
from itertools import product
import operator
from collections import defaultdict
from copy import deepcopy

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    if file_type == '0':
        return parse_file()
    return parse_file('input.txt')

def parse_file(file=None):
    rules = {}
    my_ticket = []
    nearby = []
    if file:
        with open(file, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]

    off = offset(lines)
    ymap = defaultdict(lambda: defaultdict(lambda: '.'))
    for y, yval in enumerate(lines):
        xmap = defaultdict(lambda: '.')
        for x, xval in enumerate(yval):
            xmap[x - off] = xval
        ymap[y - off] = xmap
    return ymap

def offset(state):
     return (len(state) -1) // 2

def state_range(state):
    off = offset(state)
    return [x for x in range(-1 * off, off + 1)]

def neighbours(x, y, z):
    return [tuple(map(operator.add, (x, y, z), move)) for move in product([-1, 0, 1], repeat=3) if move != (0, 0, 0)]

def get_state(state, x, y, z):
    ne = neighbours(x, y, z)
    active_count = 0
    _state = deepcopy(state)
    for _n in ne:
        if _state[_n[2]][_n[1]][_n[0]] == '#':
            active_count += 1
    if _state[z][y][x] == '#':
        return '#' if active_count in [2, 3] else '.'
    else:
        return '#' if  active_count == 3 else '.'

def neighbours2(x, y, z, w):
    return [tuple(map(operator.add, (x, y, z, w), move)) for move in product([-1, 0, 1], repeat=4) if move != (0, 0, 0, 0)]

def get_state2(state, x, y, z, w):
    ne = neighbours2(x, y, z, w)
    active_count = 0
    _state = deepcopy(state)
    for _n in ne:
        if _state[_n[3]][_n[2]][_n[1]][_n[0]] == '#':
            active_count += 1
    if _state[w][z][y][x] == '#':
        return '#' if active_count in [2, 3] else '.'
    else:
        return '#' if  active_count == 3 else '.'

def populate(state):
    _state = deepcopy(state)
    for z, zval in state.items():
        for y, yval in zval.items():
            for x, _ in yval.items():
                ne = neighbours(x, y, z)
                for _n in ne:
                    _state[_n[2]][_n[1]][_n[0]]
    return _state

def populate2(state):
    _state = deepcopy(state)
    for w, wval in state.items():
        for z, zval in wval.items():
            for y, yval in zval.items():
                for x, _ in yval.items():
                    ne = neighbours2(x, y, z, w)
                    for _n in ne:
                        _state[_n[3]][_n[2]][_n[1]][_n[0]]
    return _state

def print_map(zmap):
    for z, zdata in sorted(zmap.items()):
        print("Z=", z)
        for y, ydata in sorted(zdata.items()):
            print("".join([x for _, x in sorted(ydata.items())]))

def print_map2(wmap):
    for w, wdata in sorted(wmap.items()):
        for z, zdata in sorted(wdata.items()):
            print("Z=", z, "W=", w)
            for y, ydata in sorted(zdata.items()):
                print("".join([x for _, x in sorted(ydata.items())]))

def count_active(state):
    count = 0
    for z, zdata in sorted(state.items()):
        for y, ydata in sorted(zdata.items()):
            s = "".join([x for _, x in sorted(ydata.items())])
            count += s.count('#')
    return count

def count_active2(state):
    count = 0
    for w, wdata in sorted(state.items()):
        for z, zdata in sorted(wdata.items()):
            for y, ydata in sorted(zdata.items()):
                s = "".join([x for _, x in sorted(ydata.items())])
                count += s.count('#')
    return count

def go1():
    zmap = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.')))
    zmap[0] = lines
    new_state = deepcopy(zmap)
    for cycle in range(6):
        cur_state = populate(new_state)
        for z, zdata in sorted(cur_state.items()):
            for y, ydata in sorted(zdata.items()):
                for x, xdata in sorted(ydata.items()):
                    # print(x, y, z, cur_state[z][y][x], "->", get_state(cur_state, x, y, z))
                    new_state[z][y][x] = get_state(cur_state, x, y, z)

    print_map(new_state)
    print(count_active(new_state))


def go2():
    wmap = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.'))))
    wmap[0][0] = lines
    new_state = deepcopy(wmap)
    for cycle in range(6):
        cur_state = populate2(new_state)
        for w, wdata in sorted(cur_state.items()):
            for z, zdata in sorted(wdata.items()):
                for y, ydata in sorted(zdata.items()):
                    for x, xdata in sorted(ydata.items()):
                        # print(x, y, z, cur_state[z][y][x], "->", get_state(cur_state, x, y, z))
                        new_state[w][z][y][x] = get_state2(cur_state, x, y, z, w)

        print_map2(new_state)
    print(count_active2(new_state))


lines = get_lines(sys.argv[1])

def main():
    print(go2())

if __name__ == "__main__":
    main()

