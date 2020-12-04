#!/usr/bin/env python3

num_list = []

with open('input', 'r') as f:
    for number in f:
        num_list.append(int(number))

for number in num_list:
    for second_number in num_list:
        if number + second_number == 2020:
            print(number * second_number)
