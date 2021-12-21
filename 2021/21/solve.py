#!/usr/bin/env python3

from itertools import product
from collections import Counter
from functools import lru_cache

p1 = [0, 7]
p2 = [0, 6]
move = 0
active = p1
for d in range(1, 10000):
    move += 1
    active[1] = (active[1] + d - 1) % 10 + 1
    if move == 3:
        active[0] += active[1]
        if active[0] > 999:
            break
        active = p1 if active == p2 else p2
        move = 0

ans = min([d*p1[0], d*p2[0]])
print(f"P1 {p1}, P2 {p2}, ans {ans}")

dice = product(range(1,4), repeat=3)
dice_freq = Counter([sum(x) for x in dice])

@lru_cache(maxsize=99999999)
def take_turn(p1, p2, s1=0, s2=0):
    if s1 > 20:
        return (1, 0)
    if s2 > 20:
        return (0, 1)
    result = (0, 0)
    for dVal, freq in dice_freq.items():
        new_pos = (p1 + dVal - 1) % 10 + 1
        new_score = s1 + new_pos
        p2w, p1w = take_turn(p2, new_pos, s2, new_score)
        result = (result[0] + freq * p1w, result[1] + freq * p2w)
    return result


p1 = [0, 7]
p2 = [0, 6]
print(max(take_turn(7, 6)))
