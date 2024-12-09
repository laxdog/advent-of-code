import sys
from collections import defaultdict

def parse_file(file):
    with open(file, 'r') as f:
        return [[x for x in line.rstrip()] for line in f]

file_name = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
lines = parse_file(file_name)

mx = len(lines[0])
my = len(lines)

freqs = defaultdict(list)
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != '.':
            freqs[char].append((j, i))

def antinodes(v1, v2):
    vec_dist = ((v1[0] - v2[0]), (v1[1] - v2[1]))
    a1 = (v1[0] + vec_dist[0], v1[1] + vec_dist[1])
    a2 = (v2[0] - vec_dist[0], v2[1] - vec_dist[1])
    return a1, a2

p1_nodes = set()
p2_nodes = set()
for key, val in freqs.items():
    for i, v1 in enumerate(val):
        for j, v2 in enumerate(val):
            if i == j:
                continue

            for node in antinodes(v1, v2):
                if node[0] < 0 or node[1] < 0 or node[0] >= mx or node[1] >= my:
                    continue
                else:
                    p1_nodes.add(node)

            # Check each point on the map to see if it's a node
            for row in range(my):
                for col in range(mx):
                    delta_row1 = row - v1[1]
                    delta_col1 = col - v1[0]
                    delta_row2 = row - v2[1]
                    delta_col2 = col - v2[0]

                    if delta_row1 * delta_col2 == delta_col1 * delta_row2: # Check if the antennaes are in line
                        p2_nodes.add((col, row))

print(len(p1_nodes))
print(len(p2_nodes))