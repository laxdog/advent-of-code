#!/usr/bin/env python3

from math import prod

def do(times, dists):
    results = []
    for i in range(len(times)):
        total = 0
        for step in range(1, times[i]):
            if step * (times[i] - step) > dists[i]: total += 1
        results.append(total)
    return results

print(prod(do([60, 80, 86, 76], [601, 1163, 1559, 1300])))
print(do([60808676], [601116315591300]))
        