import sys

def parse_file(file):
    with open(file, 'r') as f:
        return [line.rstrip() for line in f]

file_name = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
lines = parse_file(file_name)

def find_xmas(l, x, y):
    max = len(l) - 1
    count = 0
    if x + 3 <= max and "".join(l[x+i][y] for i in range(4)) == 'XMAS': count += 1
    if x - 3 >= 0   and "".join(l[x-i][y] for i in range(4)) == 'XMAS': count += 1
    if y + 3 <= max and "".join(l[x][y+i] for i in range(4)) == 'XMAS': count += 1
    if y - 3 >= 0   and "".join(l[x][y-i] for i in range(4)) == 'XMAS': count += 1

    if x + 3 <= max and y + 3 <= max and "".join(l[x+i][y+i] for i in range(4)) == 'XMAS': count += 1
    if x - 3 >= 0   and y - 3 >= 0   and "".join(l[x-i][y-i] for i in range(4)) == 'XMAS': count += 1
    if x + 3 <= max and y - 3 >= 0   and "".join(l[x+i][y-i] for i in range(4)) == 'XMAS': count += 1
    if x - 3 >= 0   and y + 3 <= max and "".join(l[x-i][y+i] for i in range(4)) == 'XMAS': count += 1

    return count

def find_mas(l, x, y):
    max = len(l) - 1

    if l[x][y] != 'A': return 0

    if x - 1 < 0 or x + 1 > max: return 0
    if y - 1 < 0 or y + 1 > max: return 0

    mas = 0

    if f"{l[x-1][y-1]}{l[x+1][y+1]}" == 'MS': mas += 1
    if f"{l[x+1][y+1]}{l[x-1][y-1]}" == 'MS': mas += 1
    if f"{l[x+1][y-1]}{l[x-1][y+1]}" == 'MS': mas += 1
    if f"{l[x-1][y+1]}{l[x+1][y-1]}" == 'MS': mas += 1

    return 1 if mas == 2 else 0

total = 0
for x in range(len(lines)):
    for y in range(len(lines)):
        total += find_xmas(lines, x, y)

total2 = 0
for x in range(len(lines)):
    for y in range(len(lines)):
        total2 += find_mas(lines, x, y)

print(total)
print(total2)
