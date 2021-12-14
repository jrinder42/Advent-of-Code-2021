
"""

Advent of Code 2021 - Day 14

"""

from collections import defaultdict, Counter

template = ''
val_map = {}
with open('day14.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        if '->' in line:
            l, r = line.split(' -> ')
            val_map[l] = r
        elif line.strip():
            template = line

# Part 1

# naive solution

naive_template = template
s = ''
steps = 10
for step in range(steps):
    pieces = []
    for i in range(1, len(naive_template)):
        pair = naive_template[i - 1:i + 1]
        val = val_map[pair]

        if i == 1:
            pieces.append(f'{pair[0]}{val}{pair[1]}')
        else:
            pieces.append(f'{val}{pair[1]}')
    s = ''.join(pieces)
    naive_template = s

c = Counter(s)
most = c.most_common(1)[0][1]
least = c.most_common()[-1][1]
c = Counter(s)

print(f'Advent of Code Day 14 Answer Part 1: {most - least}')

# Part 2

# faster solution

hold = defaultdict(int)
for i in range(1, len(template)):
    pair = template[i - 1:i + 1]
    hold[pair] += 1

steps = 10
def polymer(hold, steps=1):
    for step in range(steps):
        inner = defaultdict(int)

        for pair, value in hold.items():
            val = val_map[pair]
            inner[f'{pair[0]}{val}'] += value
            inner[f'{val}{pair[1]}'] += value

        hold = inner

    return hold

hold = polymer(hold, steps=40)
hold_map = defaultdict(int)
for i, (pair, value) in enumerate(hold.items()):
    if i == 0:
        hold_map[pair[0]] += value
    hold_map[pair[1]] += value

p2 = max(hold_map.values()) - min(hold_map.values())

print(f'Advent of Code Day 14 Answer Part 2: {p2}')
