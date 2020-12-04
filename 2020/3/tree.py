#!/usr/bin/env python3

def find_trees(right, down):
    rcount = right
    dcount = down
    tree_count = 0
    with open('input', 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        while dcount < len(lines):
            tree_count += lines[dcount][rcount % len(lines[dcount])] == '#'
            rcount += right
            dcount += down

        return(tree_count)

print("trees", find_trees(3, 1))
print("trees", find_trees(1, 1) * find_trees(3, 1) * find_trees(5, 1) * find_trees(7, 1) * find_trees(1, 2))
