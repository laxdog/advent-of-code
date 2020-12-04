#!/usr/bin/env python3

pass_list = []
good_pw_count = 0
other_pw_count = 0

with open('input', 'r') as f:
    for line in f:
        bounds, char, passwd = line.split()
        lower, upper = bounds.split('-')
        pass_list.append([int(lower), int(upper), char.strip(':'), passwd])

def check_pw(lower, upper, char, pw):
    if char not in pw:
        return False
    return lower <= pw.count(char) <= upper
        
def check_other_pw(first, second, char, pw):
    try:
        if char not in pw or pw[first - 1] == char and pw[second - 1] == char:
            return False
        if pw[first - 1] == char or pw[second - 1] == char:
            return True
        return False
    except(IndexError):
        return False

for item in pass_list:
    good_pw_count += check_pw(*item)
    other_pw_count += check_other_pw(*item)

print(len(pass_list))
print(good_pw_count)
print(other_pw_count)
