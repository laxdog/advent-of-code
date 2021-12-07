#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input')
    return parse_file('sample1')

def parse_file(file):
    with open(file, 'r') as f:
        return [int(x) for  x in [line.strip().split(',') for line in f.readlines() if line.strip()][0]]

def calc_fuel(pos, crabs):
    total = 0
    for crab in crabs:
        total += abs(crab-pos)
    return total

def calc_fuel2(pos, crabs):
    total = 0
    for crab in crabs:
        total += sum([x for x in range(abs(crab - pos) + 1)])
    return total


def go():
    crabs = get_lines()
    last = sum(crabs) // len(crabs)
    fuel = 99999999
    fuel2 = 99999999
    for _ in range(200):
        fuel = calc_fuel(last, crabs) if calc_fuel(last, crabs) < fuel else fuel
        last += 1 if calc_fuel(last + 1, crabs) < calc_fuel(last, crabs) else -1

    for _ in range(200):
        fuel2 = calc_fuel2(last, crabs) if calc_fuel2(last, crabs) < fuel2 else fuel2
        last += 1 if calc_fuel2(last + 1, crabs) < calc_fuel2(last, crabs) else -1

    print(fuel)
    print(fuel2)

go()