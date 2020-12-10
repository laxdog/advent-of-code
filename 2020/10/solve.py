#!/usr/bin/env python

import sys
from collections import defaultdict
from itertools import combinations
import copy

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        lines = sorted([int(line.strip()) for line in f.readlines() if line.strip()])
        return [0] + lines + [max(lines) + 3]

def go2():
    # Each adapter is a key, the value will be the number of ways to get to it
    # Some routes are not possible because we don't have the adapter. So this will return 0 for those
    routes = defaultdict(int)
    # We already know there's only one way to get to 0
    routes[0] = 1
    # Loop each adapter we have and work out how to get there from previous ones
    for forward in range(len(lines)):
        # look through possible adapters with smaller joltage than the one we have
        for backward in reversed(range(forward)):
            # If the joltage diff is more than 3 we can never get there directly from that particular adapter.
            # But we can use the other adapters to get to it
            if lines[forward] - lines[backward] > 3:
                break
            # if we can get there, add the number of ways to get to that one to our current adapter's route list.
            # There will be up to 3, but some don't exist so will be zero (default dict)
            routes[forward] += routes[backward]
    print(routes[max(routes.keys())])



lines = get_lines(sys.argv[1])
def main():
    go2()

if __name__ == "__main__":
    main()

