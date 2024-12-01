from collections import defaultdict
import numpy as np


def get_lines(file_type=None):
    file_map = {1: 'sample1', 2: 'sample2'}
    file_name = file_map.get(file_type, 'input.txt')
    return parse_file(file_name)

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split('   ') for line in f]


left = []
right = []
for row in get_lines():
    left.append(int(row[0]))
    right.append(int(row[1]))

left.sort()
right.sort()

total = 0
for x in range(len(left)):
    total += abs(left[x] - right[x])

print(total)

total2 = 0
for num in left:
    count = right.count(num)
    total2 += count * num

print(total2)
