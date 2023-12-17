import heapq
import math

# Based on : https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/17.py
# basically a modified version of Dijkstra's algorithm

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

def is_valid_move(next_row, next_col, direction, new_dir, new_moves, moves):
    reverse = ((new_dir + 2) % 4 == direction)
    if PART1 : valid = (new_moves <= 3)
    else:      valid = (new_moves<=10 and (new_dir==direction or moves>=4 or moves==-1))
    return 0 <= next_row < ROWS and 0 <= next_col < COLS and not reverse and valid

def update_priority_queue(priority_q, r, c, direction, moves, dist, lines, directions):
    for i, (dr, dc) in enumerate(directions):
        next_row, next_col = r + dr, c + dc
        new_dir = i
        new_moves = 1 if new_dir != direction else moves + 1

        if is_valid_move(next_row, next_col, direction, new_dir, new_moves, moves):
            cost = int(lines[next_row][next_col])
            heapq.heappush(priority_q, (dist + cost, next_row, next_col, new_dir, new_moves))

def find_shortest_path(lines):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    priority_q = [(0, 0, 0, -1, -1)]
    visited = {}

    while priority_q:
        dist, r, c, direction, moves = heapq.heappop(priority_q)
        if (r, c, direction, moves) in visited:
            continue
        visited[(r, c, direction, moves)] = dist
        update_priority_queue(priority_q, r, c, direction, moves, dist, lines, directions)

    return calculate_shortest_distance(visited)

def calculate_shortest_distance(visited):
    shortest = math.inf
    for (r, c, _, _), v in visited.items():
        if r == ROWS - 1 and c == COLS - 1:
            shortest = min(shortest, v)
    return shortest

lines, ROWS, COLS = initialize_grid()
for PART1 in [True, False]:
    print(find_shortest_path(lines))