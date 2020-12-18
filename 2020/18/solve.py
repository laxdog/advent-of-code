#!/usr/bin/env python

import re
import sys
import cProfile
from itertools import product
import operator
from collections import defaultdict
from copy import deepcopy, copy

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

    return lines


def parse(expr):
    def _helper(iter):
        items = []
        for item in iter:
            if item == '(':
                result, closeparen = _helper(iter)
                if not closeparen:
                    raise ValueError("bad expression -- unbalanced parentheses")
                items.append(result)
            elif item == ')':
                return items, True
            elif item == ' ':
                pass
            else:
                items.append(item)
        return items, False
    return _helper(iter(expr))[0]

def count_list(expr):
    count = 0
    op = operator.add
    for e in expr:
        if isinstance(e, list):
            count = op(count, count_list(e))
        elif e == '+':
            op = operator.add
        elif e == '*':
            op = operator.mul
        else:
            count = op(count, int(e))
    return count

# https://www.geeksforgeeks.org/expression-evaluation/
def order(op):
    if op == '*': return 1
    if op == '+': return PLUS
    return 0

def do_op(a, b, op):
    if op == '+': return a + b
    if op == '*': return a * b

def evaluate(line):
    values = []
    ops = []
    i = 0
    while i < len(line):
        if line[i] == ' ':
            i += 1
            continue
        elif line[i] == '(':
            ops.append(line[i])
        elif line[i].isdigit():
            values.append(int(line[i]))
        elif line[i] == ')':
            while len(ops) > 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(do_op(val1, val2, op))
            ops.pop()
        else:
            while (len(ops) != 0 and order(ops[-1]) >= order(line[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(do_op(val1, val2, op))
            ops.append(line[i])
        i += 1
    
    while len(ops) > 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(do_op(val1, val2, op))
    
    return values[-1]


def go1():
    count = 0
    for line in lines:
        count += count_list(parse(line))
    print(count)

    global PLUS
    PLUS = 1
    count = 0
    for line in lines:
        count += evaluate(line)
    print(count)

    PLUS = 2
    count = 0
    for line in lines:
        count += evaluate(line)
    print(count)


lines = get_lines(sys.argv[1])

def main():
    go1()

if __name__ == "__main__":
    main()

