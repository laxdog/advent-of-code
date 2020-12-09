#!/usr/bin/env python

import sys
from collections import deque

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [int(line.strip()) for line in f.readlines() if line.strip()]


lines = get_lines(sys.argv[1])

def get_sums(dq):
    lst = []
    for i, v in enumerate(dq):
        [lst.append(v + _v) for _i, _v in enumerate(dq) if i != _i]
    return lst
        

def go1(plen=25):
    preamble = deque(lines[0:plen])
    for x in lines[plen:]:
        if x in get_sums(preamble):
            preamble.append(x)
            preamble.popleft()
        else:
            return(x)


def go2():
    invalid = go1()
    for i, _ in enumerate(lines):
        x = 0
        lst = []
        while x < invalid:
            lst.append(lines[i])
            x += lines[i]
            if x == invalid:
                return(min(lst) + max(lst))
            i += 1


def main():
    print(go1())
    print(go2())

if __name__ == "__main__":
    main()

