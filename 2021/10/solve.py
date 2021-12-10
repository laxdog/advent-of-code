#!/usr/bin/env python3

def get_lines():
    return parse_file('input')
    return parse_file('sample1')

def parse_file(file):
    with open(file, 'r') as f:
        lines = [line.strip().split()[0] for line in f.readlines() if line.strip()]
    return(lines)


def go():
    total = 0
    incomplete = []
    for line in get_lines():
        total2 = 0
        openB = ""
        corrupt = False
        for char in line:
            if char in '([{<': openB += char
            if char in ')]}>':
                rev = '(' if char == ')' else chr(ord(char)-2)
                if openB[-1] == rev:
                    openB = openB[:-1]
                else:
                    if char == ')': total += 3
                    if char == ']': total += 57
                    if char == '}': total += 1197
                    if char == '>': total += 25137
                    corrupt = True
                    break

        if not corrupt:
            print(openB)
            for char in openB[::-1]:
                if char == '(': total2 = (total2 * 5) + 1
                if char == '[': total2 = (total2 * 5) + 2
                if char == '{': total2 = (total2 * 5) + 3
                if char == '<': total2 = (total2 * 5) + 4
            incomplete.append(total2)

    print(total)
    incomplete.sort()
    print(incomplete[len(incomplete)//2])

go()