#!/usr/bin/env python

import sys
import copy

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        lines = [line.strip().split() for line in f.readlines() if line.strip()]
        return [[line[0], int(line[1])] for line in lines]


lines = get_lines(sys.argv[1])


def is_inf(inst):
    acc = 0
    seen_pos = []
    pos = 0
    while pos not in seen_pos and pos < len(inst):
        seen_pos.append(pos)
        if inst[pos][0] == 'nop':
            pos +=1
        elif inst[pos][0] == 'acc':
            acc += inst[pos][1]
            pos += 1
        elif inst[pos][0] == 'jmp':
            pos += inst[pos][1]
    return (True, acc) if pos in seen_pos else (False, acc)


def go2():
    for index, op in enumerate(lines):
        _lines = copy.deepcopy(lines)
        if op[0] == 'nop':
            _lines[index][0] = 'jmp'
        elif op[0] == 'jmp':
            _lines[index][0] = 'nop'

        if is_inf(_lines)[0]:
            pass
        else:
            print(is_inf(_lines))


def main():
    print(is_inf(lines))
    go2()

if __name__ == "__main__":
    main()

