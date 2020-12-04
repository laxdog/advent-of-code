#!/usr/bin/env python3

num_list = []

with open('input', 'r') as f:
    for number in f:
        num_list.append(int(number))

for number in num_list:
    for second_number in [x for x in num_list if x != number]:
        for third_number in [x for x in num_list if x != second_number]:
            if number + second_number + third_number == 2020:
                print(number * second_number * third_number)
