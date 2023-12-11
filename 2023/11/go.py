#!/usr/bin/env python3

import networkx as nx
import multiprocessing

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split()[0] for line in f.readlines()]

def empty_space(lines):
    rows = [r for r in range(len(lines)) if all(char != '#' for char in lines[r])]
    cols = [c for c in range(len(lines[0])) if all(lines[r][c] != '#' for r in range(len(lines[0])))]
    return rows, cols

def build_graph(lines, rows, cols, size=2):
    graph = nx.Graph()
    galaxies = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            weight = size if x in cols or y in rows else 1
            if char == '#': galaxies.append((x, y))
            if x < len(line) - 1:  graph.add_edge((x, y), (x + 1, y), weight=weight)
            if y < len(lines) - 1: graph.add_edge((x, y), (x, y + 1), weight=weight)
    return graph, galaxies

def shortest_path_length_for_pair(args):
    graph, pair = args
    return nx.shortest_path_length(graph, pair[0], pair[1], weight='weight')

def calculate_total_distance(graph, galaxies):
    total_distance = 0
    galaxy_pairs = [(graph, (galaxies[i], galaxy)) for i in range(len(galaxies)) for galaxy in galaxies[i+1:]]

    # CPU go brrrrrr
    with multiprocessing.Pool() as pool:
        distances = pool.map(shortest_path_length_for_pair, galaxy_pairs)
        total_distance = sum(distances)
    return total_distance

def go():
    lines = get_lines()
    rows, cols = empty_space(lines)
    for size in [2, 1000000]:
        graph, galaxies = build_graph(lines, rows, cols, size)
        total_distance = calculate_total_distance(graph, galaxies)
        print(total_distance)

if __name__ == '__main__':
    go()