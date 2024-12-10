import sys

def parse_file(file):
    with open(file, 'r') as f:
        return [[int(x) if x.isdigit() else x for x in line.rstrip()] for line in f]

file_name = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
lines = parse_file(file_name)

mx = len(lines[0])
my = len(lines)

heads = []
peaks = []

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if   char == 0: heads.append((j, i))
        elif char == 9: peaks.append((j, i))

def all_reachable(start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stack = [(start[0], start[1], lines[start[1]][start[0]], [(start[0], start[1])])]
    routes = []

    while stack:
        x, y, current_number, path = stack.pop()

        if (x, y) == end: routes.append(path)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < mx and 0 <= ny < my:
                next_char = lines[ny][nx]
                if isinstance(next_char, int) and next_char == current_number + 1:
                    stack.append((nx, ny, next_char, path + [(nx, ny)]))

    return routes

total1, total2 = 0, 0

for head in heads:
    for peak in peaks:
        routes = all_reachable(head, peak)
        total1 += 1 if routes else 0
        total2 += len(routes)

print(total1)
print(total2)