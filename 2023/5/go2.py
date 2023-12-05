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
    sections['seeds'] = []
    current_section = None

    for line in lines:
        line = line.strip()

        for section in sections:
            if line.startswith(section):
                current_section = section
                if current_section == 'seeds':
                    seed_ranges = [int(x) for x in line.split(':')[1].strip().split()]
                    for i in range(0, len(seed_ranges), 2):
                        start, length = seed_ranges[i], seed_ranges[i+1]
                        sections['seeds'].extend([(start, start + length)])
                break
        else:
            if current_section and line != '':
                sections[current_section].append(line)

    return sections

def range_map_transform(seed_ranges, mapping):
    new_ranges = []
    for seed_start, seed_end in seed_ranges:
        transformed = False
        for dst_s, src_s, rng in mapping:
            src_end = src_s + rng
            if seed_start < src_end and src_s < seed_end:  # Check for overlap
                intersection_start = max(seed_start, src_s)
                intersection_end = min(seed_end, src_end)
                new_ranges.append((intersection_start + (dst_s - src_s), intersection_end + (dst_s - src_s)))
                transformed = True
        if not transformed:
            new_ranges.append((seed_start, seed_end))
    return new_ranges


def main():
    sections = parse_sections(get_lines())
    seed_ranges = sections['seeds']

    for section in [x for x in sections if x != 'seeds']:
        mapping = [[int(x) for x in map.split()] for map in sections[section]]
        seed_ranges = range_map_transform(seed_ranges, mapping)

    low = min(start for start, _ in seed_ranges)
    print(low)

if __name__ == "__main__":
    main()