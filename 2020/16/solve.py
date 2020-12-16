#!/usr/bin/env python

import sys
from collections import defaultdict

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    if file_type == '0':
        return parse_file()
    return parse_file('input.txt')

def parse_file(file=None):
    rules = {}
    my_ticket = []
    nearby = []
    if file:
        with open(file, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]

    for line in lines:
        if 'or' in line:
            text = line.split(':')[0]
            r1, r2 = line.split(':')[1].split(" or ")
            r1 = range(int(r1.split('-')[0]), int(r1.split('-')[1]) + 1)
            r2 = range(int(r2.split('-')[0]), int(r2.split('-')[1]) + 1)
            rules[text] = (r1, r2)
        if len(my_ticket) == 0 and ',' in line:
            my_ticket = [int(x) for x in line.split(',')]
        elif ',' in line:
            nearby.append([int(x) for x in line.split(',')])

    return rules, my_ticket, nearby

rules, my, near = get_lines(sys.argv[1])

def go1():
    invalid = 0
    for ticket in near:
        for field in ticket:
            found = False
            for name, rule in rules.items():
                if field in rule[0] or field in rule[1]:
                    found = True
            if not found:
                invalid += field

    return invalid
    # 656608 high

def go2():
    invalid = 0
    valid = []
    for ticket in near:
        found_ticket = True
        for field in ticket:
            found = False
            for name, rule in rules.items():
                if field in rule[0] or field in rule[1]:
                    found = True
            if not found:
                invalid += field
                found_ticket = False
        if found_ticket:
            valid.append(ticket)

    all_outcomes = []
    for _ in my:
        all_outcomes.append(rules.keys())
    for ticket in valid:
        pos_fields = []
        for pos, field in enumerate(ticket):
            pos_fields.append([])
            for name, rule in rules.items():
                if field in rule[0] or field in rule[1]:
                    pos_fields[pos].append(name)
                # else:
                #     all_outcomes[pos] = [p for p in all_outcomes[pos] if p != name]
            all_outcomes[pos] = [p for p in pos_fields[pos] if p in all_outcomes[pos]]
        # print([len(x) for x in all_outcomes])
    found_fields = []
    indices = []
    while len(found_fields) < 6:
        for i, field in enumerate(all_outcomes):
            field = [x for x in field if x not in found_fields]
            departs = [x for x in field if 'depart' in x]
            if len(departs) == 1:
                found_fields.append(departs[0])
                indices.append(i)
            print(len(departs), len(field), i, departs)
    print(indices)
    res = 1
    for index in indices:
        res *= my[index]
    return(res)


# time = 8
# date = 17
# plat = 14
# trak = 11
# loc  = 1
# sta  = 6

def main():
    # print(go1())
    print(go2())
    print(my[8] * my[17] * my[14] * my[11] * my[1] * my[6])

if __name__ == "__main__":
    main()

