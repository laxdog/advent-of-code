#!/usr/bin/env python3

import networkx as nx

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split()[0] for line in f.readlines()]

def go():
    lines = get_lines()
    graph = nx.Graph()
    start = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '.': continue
            if char == 'S':
                start = (x, y)
                print("Start: ", start)
                char = 'F' # hardcoded sample 2
                char = 'J' # hardcoded input
            if char in '|-LJ7F':
                if char == '|':
                    if y > 0            and lines[y-1][x] in '|7F': graph.add_edge((x, y), (x, y-1))
                    if y < len(lines)-1 and lines[y+1][x] in '|LJ': graph.add_edge((x, y), (x, y+1))
                if char == '-':
                    if x > 0            and lines[y][x-1] in '-LF': graph.add_edge((x, y), (x-1, y))
                    if x < len(line)-1  and lines[y][x+1] in '-7J': graph.add_edge((x, y), (x+1, y))
                if char == 'L':
                    if y > 0            and lines[y-1][x] in '|7F': graph.add_edge((x, y), (x, y-1))
                    if x < len(line)-1  and lines[y][x+1] in '-J7': graph.add_edge((x, y), (x+1, y))
                if char == 'J':
                    if y > 0            and lines[y-1][x] in '|F7': graph.add_edge((x, y), (x, y-1))
                    if x > 0            and lines[y][x-1] in '-FL': graph.add_edge((x, y), (x-1, y))
                if char == '7':
                    if y < len(lines)-1 and lines[y+1][x] in '|LJ': graph.add_edge((x, y), (x, y+1))
                    if x > 0            and lines[y][x-1] in '-FL': graph.add_edge((x, y), (x-1, y))
                if char == 'F':
                    if y < len(lines)-1 and lines[y+1][x] in '|LJ': graph.add_edge((x, y), (x, y+1))
                    if x < len(line)-1  and lines[y][x+1] in '-J7': graph.add_edge((x, y), (x+1, y))



    shortest_path_lengths = nx.single_source_shortest_path_length(graph, start)
    print(max(shortest_path_lengths.values()))

go()