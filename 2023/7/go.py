#!/usr/bin/env python3

from collections import defaultdict, Counter, OrderedDict

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().split() for line in f.readlines()]

def rank(hand, wild=False):
    hex = []
    for card in hand:
        if card.isdigit(): hex.append(card[0])
        elif card == 'T': hex.append('a')
        elif card == 'J' and wild: hex.append('1')
        elif card == 'J': hex.append('b')
        elif card == 'Q': hex.append('c')
        elif card == 'K': hex.append('d')
        elif card == 'A': hex.append('e')
    frequency = Counter(hex)
    s_hex = sorted(hex, key=lambda x: (-frequency[x], x))
    if '1' in s_hex:
        try:                best = [x for x in frequency.most_common() if x[0] != '1'][0][0]
        except IndexError:  best = '1' # Hand of Jokers
            
        for i, card in enumerate(s_hex):
            if card == '1': s_hex[i] = best
        frequency = Counter(s_hex)
        s_hex = sorted(s_hex, key=lambda x: (-frequency[x], x))


    def scale(rank): return int(str(rank) + ''.join(hex), 16)
    if [s_hex[0]] * 5 == s_hex:                                       return scale(7)
    if [s_hex[0]] * 4 == s_hex[:4]:                                   return scale(6)
    if [s_hex[0]] * 3 == s_hex[:3] and [s_hex[4]] * 2 == s_hex[3:]:   return scale(5)
    if [s_hex[0]] * 3 == s_hex[:3]:                                   return scale(4)
    if [s_hex[0]] * 2 == s_hex[:2] and [s_hex[2]] * 2 == s_hex[2:4]:  return scale(3)
    if [s_hex[0]] * 2 == s_hex[:2]:                                   return scale(2)
    return                                                                   scale(1)

def go():
    lines = get_lines()
    for x in [False, True]:
        total = 0
        sorted_list = sorted(lines, key=lambda pair: rank(pair[0], x))
        for i, hand in enumerate(sorted_list):
            total += int(hand[1]) * (i + 1)
        print(total)

go()