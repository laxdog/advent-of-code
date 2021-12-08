#!/usr/bin/env python3

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
# 
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# 0 - 6
# 1 - 2*
# 2 - 5
# 3 - 5
# 4 - 4*
# 5 - 5
# 6 - 6
# 7 - 3*
# 8 - 7*
# 9 - 6

# a - 8
# b - 6*
# c - 8
# d - 7
# e - 4*
# f - 9*
# g - 7

nums = {
    "0": "abcefg",
    "1": "cf",
    "2": "acdeg",
    "3": "acdfg",
    "4": "bcdf",
    "5": "abdfg",
    "6": "abdefg",
    "7": "acf",
    "8": "abcdefg",
    "9": "abcdfg"
}

from collections import defaultdict

def get_lines(file_type=None):
    if file_type == '1':
        return parse_file('sample1')
    if file_type == '2':
        return parse_file('sample2')
    return parse_file('input')
    return parse_file('sample2')
    return parse_file('sample1')

def parse_file(file):
    with open(file, 'r') as f:
        lines = [line.strip().split(',') for line in f.readlines() if line.strip()]
        out = []
        for line in lines:
            x, y = line[0].split(" | ")
            x = [x1 for x1 in x.split(" ")]
            y = [y1 for y1 in y.split(" ")]
            out.append((x, y))
        return out

def strDiff(s1, s2):
    out = []
    for s in s1:
        if s not in s2:
            out.append(s)
    for s in s2:
        if s not in s1:
            out.append(s)
    out = set(out)
    return "".join(out)

def go():
    data = get_lines()
    p1cnt = 0
    for inputs, outputs in data:
        for output in outputs:
            if len(output) in [2, 4, 3, 7]:
                p1cnt += 1
    print(p1cnt)

    final_tot = 0
    for inputs, outputs in data:
        decoded = defaultdict(str)
        decCount = defaultdict(int)
        digits = ['']*9
        for input in inputs:
            if len(input) == 2:
                digits[1] = input
            if len(input) == 4:
                digits[4] = input
            if len(input) == 3:
                digits[7] = input
            if len(input) == 7:
                digits[8] = input
        decoded['a'] = strDiff(digits[7], digits[1])
        decoded['bd'] = strDiff(digits[1], digits[4])
        decoded['eg'] = strDiff(decoded['a'], strDiff(digits[8], digits[4]))
        for input in inputs:
            for let in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
                if let in input:
                    decCount[let] += 1
        for let, cnt in decCount.items():
            if cnt == 6:
                decoded['b'] = let
            if cnt == 4:
                decoded['e'] = let
            if cnt == 9:
                decoded['f'] = let

        decoded['d'] = strDiff(decoded['bd'], decoded['b'])
        decoded['g'] = strDiff(decoded['eg'], decoded['e'])
        # Here we have a,b, ,d,e,f,g
        all = "".join([decoded[x] for x in ['a', 'b', 'd', 'e', 'f', 'g']])
        decoded['c'] = strDiff(all, "abcdefg")

        final_num = ""
        for output in outputs:
            for num, val in nums.items():
                coded = ""
                for segment in val:
                    coded += decoded[segment]
                if len(strDiff(coded, output)) == 0:
                    final_num += num


                        
        #   print(num, digits, decoded)
        print(final_num)
        final_tot += int(final_num)
    print(final_tot)

go()
