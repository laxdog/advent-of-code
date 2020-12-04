#!/usr/bin/env python3

import string

class passport(object):
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid='666'):
        self.checks = 0
        self.checks += 1920 <= int(byr) <= 2002
        self.checks += 2010 <= int(iyr) <= 2020
        self.checks += 2020 <= int(eyr) <= 2030
        self.checks += hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76
        self.checks += hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193
        self.checks += hcl[0] == '#' and all(c in string.hexdigits for c in hcl[1:])
        self.checks += ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        self.checks += len(pid) == 9 and pid.isdigit()


def find_pps():
    with open('input', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        index = 0
        pps = [" "]
        for line in lines:
            if len(line) == 0:
                index += 1
                pps.append(" ")
            else:
                pps[index] += f" {line}"

        obj_list = []
        for pp in pps:
            pass_dict = {item.split(':')[0]:item.split(':')[1] for item in pp.split()}
            try:
                obj_list.append(passport(**pass_dict))
            except(TypeError) as e:
                pass
        print(len(obj_list))
        print(len([x for x in obj_list if x.checks == 7]))

find_pps()
