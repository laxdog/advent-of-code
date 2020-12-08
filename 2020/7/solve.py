#!/usr/bin/env python

import sys

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input.txt')

def parse_file(file):
    with open(file, 'r') as f:
        return [line.strip().rstrip('.') for line in f.readlines() if line.strip()]

def parse_data():
    rules_dict = {}
    for rule in lines:
        rules_dict[rule.split(" bags contain ")[0]] = rule.split(" bags contain ")[1].split(',')
    for colour, rules in rules_dict.items():
        rules_dict[colour] = {" ".join(rule.split()[1:3]):int(rule.split()[0]) for rule in rules if 'other bags' not in rule}

    return rules_dict

def contains(rules, colour):
    def _contains(colour, num):
        count = 0
        for key, _ in rules[colour].items():
            count += _contains(key, rules[colour][key] * num)
        count += num
        return count

    count = 0
    for key, _ in rules[colour].items():
        count += _contains(key, rules[colour][key])

    return count

lines = get_lines(sys.argv[1])

def main():
    rules = parse_data()
    print(contains(rules, "shiny gold"))

if __name__ == "__main__":
    main()

