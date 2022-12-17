#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

lines = get_lines()
signals = set()
beacons = set()
for line in lines:
    parse = line.replace(',', ' ').replace(':', ' ').replace('=', ' ').split()
    sx, sy = [int(c) for c in (parse[3], parse[5])]
    bx, by = [int(c) for c in (parse[-3], parse[-1])]
    m = abs(sx - bx) + abs(sy - by)
    signals.add((sx, sy, m))
    beacons.add((bx, by))

def covered(x, y):
    for sx, sy, m in signals:
        mxy = abs(x-sx)+abs(y-sy)
        if mxy <= m and (x, y) not in beacons: return True
    return False

# Get each point just outside the range of a signal
to_check = set()
for sx, sy, m in signals:
    m += 1 # go beyond signal range
    for sig in range(m + 1 + 1):
        sx1, sy1 = sx + sig - (m + 0), sy + sig
        sx2, sy2 = sx + sig - (m + 0), sy - sig
        sx3, sy3 = sx - sig + (m + 0), sy + sig
        sx4, sy4 = sx - sig + (m + 0), sy - sig

        if 0 < sx1 < 4_000_000 and 0 < sy1 < 4_000_000: to_check.add((sx1, sy1))
        if 0 < sx2 < 4_000_000 and 0 < sy2 < 4_000_000: to_check.add((sx2, sy2))
        if 0 < sx3 < 4_000_000 and 0 < sy3 < 4_000_000: to_check.add((sx3, sy3))
        if 0 < sx4 < 4_000_000 and 0 < sy4 < 4_000_000: to_check.add((sx4, sy4))


count = 0
for i in range(-10_000_000, 10_000_000):
    if covered(i, 2_000_000):
        count += 1
print("Part 1:", count)

for x, y in to_check:
    if not covered(x, y):
        print("Part 2:", (x * 4_000_000) + y)
