#!/usr/bin/env python3

def get_lines(file_type=None):
    if file_type == 1: return parse_file('sample1')
    if file_type == 2: return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

def go(file_type=None):
    total = 0
    total2 = 0
    games = {}
    for line in get_lines(file_type):
        game = int(line.split(':')[0].replace('Game ', ''))
        games[game] = {}
        valid = True
        for colour in ['blue', 'green', 'red']:
            games[game][colour] = 0
        for pull in line.split(':')[1].strip().split(';'):
            for cubes in pull.split(', '):
                for colour in ['blue', 'green', 'red']:
                    if colour in cubes:
                        if int(cubes.split(colour)[0]) > games[game][colour]:
                            games[game][colour] = int(cubes.split(colour)[0])
                if games[game]['red']   > 12: valid = False
                if games[game]['green'] > 13: valid = False
                if games[game]['blue']  > 14: valid = False

        if valid:
            total += game
        total2 += games[game]['red'] * games[game]['green'] * games[game]['blue']


    print(total, total2)
go()
