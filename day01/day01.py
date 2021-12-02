
"""

Advent of Code 2021 - Day 1

"""

vals = []
with open('day01.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        vals.append(float(line))

inc = 0
for i in range(1, len(vals)):
    if vals[i] - vals[i - 1] > 0:
        inc += 1

print(f'Advent of Code Day 1 Answer Part 1: {inc}')

inc = 0
for i in range(len(vals) - 3):
    nums_1 = vals[i:i + 3]
    nums_2 = vals[i + 1:i + 3 + 1]
    if sum(nums_2) - sum(nums_1) > 0:
        inc += 1

print(f'Advent of Code Day 1 Answer Part 2: {inc}')






