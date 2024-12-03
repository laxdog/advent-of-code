import sys

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split() for line in f]

def is_safe(rule):
    is_sorted = (rule == sorted(rule) or rule == sorted(rule, reverse=True))
    safe = True
    for i in range(len(rule[:-1])):
        if not 1 <= abs(rule[i] - rule[i + 1]) <= 3:
            safe = False
    return is_sorted and safe

def safe_with_dampener(rule):
    safe = False
    for i in range(len(row)):
        rule = row[:i] + row[i + 1:]
        if is_safe(rule):
            safe = True
            break
    return safe
 
file_name = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
lines = parse_file(file_name)

total = 0
total2 = 0

for row in lines:
    row = list(map(int, row))
    if is_safe(row): total += 1
    if safe_with_dampener(row): total2 += 1

print(total)
print(total2)