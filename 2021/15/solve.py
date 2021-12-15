#!/usr/bin/env python3

import networkx as nx

def get_lines(file_type=None):
    return parse_file('input')
    return parse_file('sample1')
    return parse_file(0)

def parse_file(file):
    with open(file, 'r') as f:
        return [[int(x) for x in line.strip()] for line in f.readlines() if line.strip()]
        
def get_graph(lines):
    my, mx = (len(lines), len(lines[0]))
    G = nx.DiGraph()
    for y in range(my):
        for x in range(mx):
            G.add_node((x, y))

            for x1, y1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newx = x + x1
                newy = y + y1
                if mx > newx >= 0 and my > newy >= 0:
                    G.add_edge((x, y), (newx, newy), weight=lines[newy][newx])

    return G


def go():
    lines = get_lines()
    my = len(lines)
    mx = len(lines[0])

    start = (0, 0)

    for scale in [1, 5]:
        data = [0] * (scale * my)
        for y in range(my):
            for s in range(scale):
                data[my * s + y] = lines[y] * scale

        for s1 in range(scale):
            for s2 in range(scale):
                if s1 == 0 and s2 == 0:
                    continue

                for y1 in range(my):
                    for x1 in range(mx):
                        x = s1 * len(lines) + y1
                        y = s2 * len(lines) + x1
                        data[y][x] += (s1 + s2)
                        if data[y][x] > 9:
                            data[y][x] = data[y][x] % 9

        end = ((mx*scale)-1, (my*scale)-1)
        G = get_graph(data)
        path = nx.shortest_path(G, source=start, target=end, weight='weight')
        print(sum([data[y][x] for x, y in path[1:]]))


go()
