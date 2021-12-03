
"""

Advent of Code 2021 - Day 3

"""

from collections import defaultdict, Counter

l = 0
d = defaultdict(list)
with open('day03.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        l = len(line)
        for i in range(l):
            d[i].append(line[i])

# Part 1

gamma = []
epsilon = []
for key, value in d.items():
    x = Counter(value)
    if x['1'] > x['0']:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

print(f'Advent of Code Day 3 Answer Part 1: {gamma * epsilon}')

# Part 2

l = 0
d = defaultdict(list)
vals = []
with open('day03.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        l = len(line)
        for i in range(l):
            d[i].append(line[i])
        vals.append(line)

scrub = vals.copy()

c = 0
while len(vals) > 1:
    dd = defaultdict(list)
    for val in vals:
        for i in range(l):
            dd[i].append(val[i])

    key = c
    x = Counter(dd[c])
    if x['1'] >= x['0']:
        to_delete = []
        for val in vals:
            if val[key] != '1':
                to_delete.append(val)

        for val in to_delete:
            vals.remove(val)

    elif x['1'] < x['0']:
        to_delete = []
        for val in vals:
            if val[key] != '0':
                to_delete.append(val)

        for val in to_delete:
            vals.remove(val)

    c += 1

oxygen = int(''.join(vals), 2)

c = 0
while len(scrub) > 1:
    dd = defaultdict(list)
    for val in scrub:
        for i in range(l):
            dd[i].append(val[i])

    key = c
    x = Counter(dd[c])
    if x['1'] >= x['0']:
        to_delete = []
        for val in scrub:
            if val[key] != '0':
                to_delete.append(val)

        for val in to_delete:
            scrub.remove(val)

    elif x['1'] < x['0']:
        to_delete = []
        for val in scrub:
            if val[key] != '1':
                to_delete.append(val)

        for val in to_delete:
            scrub.remove(val)

    c += 1

scrubber = int(''.join(scrub), 2)

print(f'Advent of Code Day 3 Answer Part 2: {oxygen * scrubber}')