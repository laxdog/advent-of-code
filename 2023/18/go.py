from collections import defaultdict
import numpy as np
from skimage.morphology import flood_fill


def get_lines(file_type=None):
    file_map = {1: 'sample1', 2: 'sample2'}
    file_name = file_map.get(file_type, 'input.txt')
    return parse_file(file_name)

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split() for line in f]


grid = defaultdict(dict)
location = (0, 0)
min_x, max_x, min_y, max_y = 0, 0, 0, 0

for dir, size, _ in get_lines():
    size = int(size)
    for d in range(size):
        if dir == 'R': location = (location[0] + 1, location[1])
        elif dir == 'L': location = (location[0] - 1, location[1])
        elif dir == 'U': location = (location[0], location[1] - 1)
        elif dir == 'D': location = (location[0], location[1] + 1)

        min_x = min(min_x, location[0])
        max_x = max(max_x, location[0])
        min_y = min(min_y, location[1])
        max_y = max(max_y, location[1])

        grid[location[0]][location[1]] = '#'

np_grid = np.zeros((max_x - min_x + 1, max_y - min_y + 1), dtype=np.uint8)
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if x in grid and y in grid[x]:
            np_grid[x - min_x, y - min_y] = 1


# lazy start point, this is correct for the input, not the sample
ff = flood_fill(np_grid, (max_x, max_y), 1)
print(np.count_nonzero(ff))

# Part 2
def parse_colour(colour):
    size = int(colour[2:7], 16)
    if colour[7] == '0': dir = 'R'
    elif colour[7] == '1': dir = 'D'
    elif colour[7] == '2': dir = 'L'
    elif colour[7] == '3': dir = 'U'
    return dir, size


points = []
location = (0, 0)
min_x, max_x, min_y, max_y = 0, 0, 0, 0

for dir, size, colour in get_lines():
    dir, size = parse_colour(colour)
    if dir == 'R': location = (location[0] + size, location[1])
    elif dir == 'L': location = (location[0] - size, location[1])
    elif dir == 'U': location = (location[0], location[1] - size)
    elif dir == 'D': location = (location[0], location[1] + size)

    min_x = min(min_x, location[0])
    max_x = max(max_x, location[0])
    min_y = min(min_y, location[1])
    max_y = max(max_y, location[1])

    points.append(location)

def shoelace_area(vertices):
    n = len(vertices)
    area = 0
    perimeter_length = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
        perimeter_length += ((vertices[j][0] - vertices[i][0])**2 + (vertices[j][1] - vertices[i][1])**2)**0.5
    return abs(area) / 2, perimeter_length

def total_area_with_perimeter(vertices):
    interior_area, perimeter_length = shoelace_area(vertices)
    perimeter_area = perimeter_length
    return interior_area + perimeter_area / 2 + 1 # +1 for the starting point

print(total_area_with_perimeter(points))