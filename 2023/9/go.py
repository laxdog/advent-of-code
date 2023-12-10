#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [[int(x) for x in line.strip().split()] for line in f.readlines()]


def evaluate_sequence(sequence, backwards):
    all_zeros = True
    for x in sequence:
        if x != 0:
            all_zeros = False
            break
    if all_zeros: return 0

    differences = []
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        differences.append(diff)

    if backwards: return sequence[0] - evaluate_sequence(differences, backwards)
    else:         return sequence[-1] + evaluate_sequence(differences, backwards)

lines = get_lines()
for backwards in [False, True]:
    total = 0
    for line in lines:
        total += evaluate_sequence(line, backwards)
    print(total)
