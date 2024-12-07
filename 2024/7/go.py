import os
import sys
import time
from itertools import product

def parse_file(file):
    with open(file, 'r') as f:
        return [line.rstrip().replace(":", "") for line in f]

file_name = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
lines = parse_file(file_name)

def find_combos(numbers, ops):
    results = []

    for combination in product(ops, repeat=len(numbers) - 1):
        temp = []
        for i, item in enumerate(numbers):
            temp.append(item)
            if i < len(combination):
                temp.append(combination[i])
        results.append(temp)

    return results

def calc(combo):
    # Ignore BIDMAS
    total = combo.pop(0)
    while combo:
        op = combo.pop(0)
        num = combo.pop(0)
        if   op == '+': total += num
        elif op == '*': total *= num
        elif op == '|': total = int(f"{total}{num}")
    return total
part1, part2, tried = [0]*3

ops_lists = {
    'part1': ['+', '*'],
    'part2': ['+', '*', '|']
}

for line in lines:
    total, *numbers = map(int, line.split(' '))

    for part, ops_to_try in ops_lists.items():
        combos = find_combos(numbers, ops_to_try)

        for combo in combos:
            tried += 1
            print(f"Tried: {tried}", end='\r')

            if calc(combo) == total:
                if   part == 'part1': part1 += total
                elif part == 'part2': part2 += total
                break

print("\n", part1)
print(part2)
