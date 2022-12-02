#!/usr/bin/env python3

import sys

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def go():
    score, score2 = 0, 0
    score2 = 0 
    for round in get_lines():
        opp, me = round.split(' ')
        if opp == 'A': opp = 'X'
        if opp == 'B': opp = 'Y'
        if opp == 'C': opp = 'Z'
        opp = ord(opp) - 87
        me = ord(me) - 87
        score += me
        if opp == me:
            score +=3
        if (opp == 1 and me == 2) or (opp == 2 and me == 3) or(opp == 3 and me == 1):
            score +=6

        if me == 1:
            score2 += 0
            if opp == 1: score2 += 3
            else: score2 += (opp - 1)
        if me == 2:
            score2 += 3
            score2 += opp
        if me == 3:
            score2 += 6
            if opp == 3: score2 += 1
            else: score2 += (opp + 1)

    print(score)
    print(score2)


go()
