from collections import defaultdict

def get_lines(file_type=None):
    file_map = {1: 'sample1', 2: 'sample2'}
    file_name = file_map.get(file_type, 'input.txt')
    return parse_file(file_name)

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split()[0] for line in f]


def hash_of(string):
    total = 0
    for char in string:
        total += ord(char)
        total *= 17
        total %= 256
    return total

strings = get_lines()[0]
result = 0
for string in strings.split(","):
    result += hash_of(string)
print(result)

boxes = defaultdict(list)

for step in strings.split(","):
    focal = None
    if '-' in step:
        label = step.split('-')[0]
    if '=' in step:
        label, focal = step.split('=')
    box = hash_of(label)

    if focal:
        found = False
        for i, lens in enumerate(boxes[box]):
            if label in lens:
                boxes[box][i] = f"{label} {focal}"
                found = True
                break
        if not found: boxes[box].append(f"{label} {focal}")
    else:
        for i, lens in enumerate(boxes[box]):
            if label in lens:
                boxes[box].pop(i)
                break

result = 0
for i, box in boxes.items():
    for j, lens in enumerate(box):
        total = (i + 1) * (j + 1) * int(lens.split(' ')[1])
        result += total

print(result)