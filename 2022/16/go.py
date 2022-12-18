#!/usr/bin/env python3

from collections import defaultdict
from copy import deepcopy
from time import sleep
import os

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split() for line in f.readlines()]

lines = get_lines(1)
valves = {}
for line in lines:
    valve, rate, to = line[1], line[4].split('=')[1].replace(';',''), [x.replace(',', '') for x in line[9:]]
    valves[valve] = {'flow': int(rate), 'to': to}
print(valves)

time = 30
pressure = 0
on = set()
location = 'AA'
while time != 0:
    sleep(.3)
    print(f"Move to {location}: {valve}")
    valve = valves[location]
    exits = valve['to']
    if valve['flow'] == 0:
        on.add(location)
    if location not in on:
        on.add(location)
        print(f"Turn on {location}")
        time -= 1 # Turn it on
        pressure += time * valve['flow']
    for v_to in valve['to']:
        if v_to not in on:
            location = v_to
            time -= 1 # Move


