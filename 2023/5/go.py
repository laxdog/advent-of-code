#!/usr/bin/env python3

from collections import defaultdict

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse_sections(lines):
    sections = {
        'seeds': [],
        'seed-to-soil map': [],
        'soil-to-fertilizer map': [],
        'fertilizer-to-water map': [],
        'water-to-light map': [],
        'light-to-temperature map': [],
        'temperature-to-humidity map': [],
        'humidity-to-location map': []
    }

    current_section = None

    for line in lines:
        line = line.strip()

        for section in sections:
            if line.startswith(section):
                current_section = section
                if current_section == 'seeds':
                    sections['seeds'] = [int(x) for x in line.split(':')[1].strip().split()]
                break
        else:
            if current_section and line != '':
                sections[current_section].append(line)

    return sections

sections = parse_sections(get_lines())

final_map = defaultdict(list)
for seed in sections['seeds']:
    final_map[seed].append(seed)

for seed, values in final_map.items():
    for section in [x for x in sections if x != 'seeds']:
        for map in sections[section]:
            last_value = values[-1]
            dst_s, src_s, rng = [int(x) for x in map.split()]
            if src_s <= last_value < src_s + rng:
                final_map[seed].append(last_value + (dst_s - src_s))
                break
            else:
                final_map[seed].append(last_value)

low = min([values[-1] for values in final_map.values()])
print(low)