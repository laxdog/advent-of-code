#!/usr/bin/env python3

from collections import defaultdict

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def go(file_type=None):
    fs = defaultdict(int)
    for line in get_lines(file_type):
        if line.startswith('$ cd /'): cwd = ['']
        elif line.startswith('$ ls'): pass
        elif line.startswith('dir '): pass
        elif line.startswith('$ cd'):
            if '..' in line: cwd.pop(-1)
            else: cwd.append(line.split()[-1] + '/')
        else:
            for index, dir in enumerate(cwd):
                abs_dir = "".join(cwd[:index]) + dir
                fs[abs_dir] += int(line.split()[0])

    print(sum([x for x in fs.values() if x <= 100000]))
    print(min([x for x in fs.values() if x >= fs[''] - (70000000 - 30000000)]))

go()
