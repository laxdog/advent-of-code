import re
import sys

def parse_file(file):
    with open(file, 'r') as f:
        return [line.rstrip() for line in f]

file_name = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
lines = parse_file(file_name)

def calc_mul(matches):
    total = 0
    for match in matches:
        match = match.replace("mul", "").replace("(", "").replace(")", "").replace(",", "*")
        match = match
        total += eval(match)
    return total


def find_mul_after_do(text):
    pattern = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"
    matches = re.findall(pattern, text)

    results = []
    searching = True

    for match in matches:
        if match == "do()":
            searching = True
        elif match == "don't()":
            searching = False
        elif searching and match.startswith("mul("):
            results.append(match)

    return results

pattern = r"mul\(\d+,\d+\)"
text = "\n".join(lines)
matches = re.findall(pattern, text)

total = calc_mul(matches)
print(total) # == 159833790)

matches = find_mul_after_do(text)
total = calc_mul(matches)
print(total) # == 89349241)