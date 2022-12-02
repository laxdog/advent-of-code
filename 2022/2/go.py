#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def go(file_type=None):
    score, score2 = 0, 0
    for round in get_lines(file_type):
        opp, me = round.split(' ')
        opp = ord(opp) - ord('A') + 1
        me = ord(me) - ord('X') + 1
        score += me
        if opp == me: score += 3
        if (opp - me) % 3 == 2: score += 6
        # Part 2
        if me == 1:
            if opp == 1: score2 += 3
            else: score2 += (opp - 1)
        if me == 2: score2 += 3 + opp
        if me == 3:
            score2 += 6
            if opp == 3: score2 += 1
            else: score2 += (opp + 1)

    print(score)
    print(score2)


go(1)
go()
