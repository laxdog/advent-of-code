from collections import defaultdict
import sys

sys.setrecursionlimit(10000)  # Set a higher recursion limit

def get_lines(file_type=None):
    file_map = {1: 'sample1', 2: 'sample2'}
    file_name = file_map.get(file_type, 'input.txt')
    return parse_file(file_name)

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split()[0] for line in f]


def initialize_grid():
    lines = get_lines()
    return lines, len(lines), len(lines[0])


GRID, ROWS, COLS = initialize_grid()

ENGERGISED = set()

def do_beam(r, c, dir, path):
    if (r, c, dir) in path: # Avoid infinite loops
        return

    if not (0 <= r < ROWS and 0 <= c < COLS):
        return

    path.add((r, c, dir))
    ENGERGISED.add((r, c))

    next_r, next_c = r + dir[0], c + dir[1]
    current_tile = GRID[r][c]

    if current_tile == '.':
        do_beam(next_r, next_c, dir, path)

    if current_tile == '|':
        if dir[1] == 0: do_beam(next_r, next_c, dir, path)
        else:
            do_beam(r, c, (-1, 0), path)
            do_beam(r, c,  (1, 0), path)

    if current_tile == '-':
        if dir[0] == 0: do_beam(next_r, next_c, dir, path)
        else:
            do_beam(r, c, (0, -1), path)
            do_beam(r, c,  (0, 1), path)

    if current_tile == '/':
        if dir   == (0,  1): new_dir = (-1, 0) # Moving right
        elif dir == (1,  0): new_dir = (0, -1) # Moving down
        elif dir == (0, -1): new_dir = (1, 0)  # Moving left
        elif dir == (-1, 0): new_dir = (0, 1)  # Moving up
        do_beam(r + new_dir[0], c + new_dir[1], new_dir, path)

    if current_tile == '\\':
        if dir   == (0,  1): new_dir = (1,  0) # Moving right
        elif dir == (1,  0): new_dir = (0,  1) # Moving down
        elif dir == (0, -1): new_dir = (-1, 0) # Moving left
        elif dir == (-1, 0): new_dir = (0, -1) # Moving up
        do_beam(r + new_dir[0], c + new_dir[1], new_dir, path)


do_beam(0, 0, (0, 1), set())
print(len(ENGERGISED))

most = 0
for c in range(COLS):
    ENGERGISED.clear()
    do_beam(0, c, (1, 0), set())
    most = max(most, len(ENGERGISED))

for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    for start in [(0, 0), (0, COLS - 1), (ROWS - 1, 0), (ROWS - 1, COLS - 1)]:
        # Reset ENGERGISED set for each new configuration
        ENGERGISED.clear()
        do_beam(start[0], start[1], direction, set())
        most = max(most, len(ENGERGISED))
print(most)



def visualize():
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in ENGERGISED:
                print('#', end='')
            else:
                print(GRID[r][c], end='')
        print()

# visualize()