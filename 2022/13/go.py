#!/usr/bin/python3
import sys
from functools import cmp_to_key

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line for line in f.read().split('\n\n')]

lines = get_lines()

def check_all(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right: return False
        if left < right: return True
        if left == right: return None

    elif isinstance(left, list) and isinstance(right, list):
        for i in range(max(len(left), len(right))):
            try:
                ordered = check_all(left[i], right[i])
                if ordered is not None: return ordered
            except IndexError:
                return len(left) < len(right)

    elif isinstance(left, list) and isinstance(right, int): return check_all(left, [right])
    elif isinstance(left, int) and isinstance(right, list): return check_all([left], right)
    else: print("Something went wrong", type(left), type(right))


def mycmp(a, b):
    if check_all(a, b): return -1
    else: return 1


index = 0
total = 0
packets = [[[2]],[[6]]]
for line in lines:
    left = eval(line.split('\n')[0])
    right = eval(line.split('\n')[1])
    packets.append(left)
    packets.append(right)
    index += 1
    if check_all(left, right):
        total += index

print(total)

sort_pack = sorted(packets, key=cmp_to_key(mycmp))
print((sort_pack.index([[2]]) + 1) * (sort_pack.index([[6]]) + 1))
