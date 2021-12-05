
"""

Advent of Code 2021 - Day 5

"""

from collections import defaultdict

# Part 1

points = defaultdict(int)
with open('day05.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        start, end = line.split(' -> ')
        x1, y1 = start.split(',')
        x1, y1 = int(x1), int(y1)
        x2, y2 = end.split(',')
        x2, y2 = int(x2), int(y2)
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                small, large = min(y1, y2), max(y1, y2)
                for i in range(small, large + 1):
                    points[(x1, i)] += 1
            elif y2 == y2:
                small, large = min(x1, x2), max(x1, x2)
                for i in range(small, large + 1):
                    points[(i, y1)] += 1

count = 0
for key, value in points.items():
    if value > 1:
        count += 1

print(f'Advent of Code Day 5 Answer Part 1: {count}')

# Part 2

# was watching the big-10 championship trophy ceremony -- twas a bit distracted

points = defaultdict(int)
with open('day05.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        start, end = line.split(' -> ')
        x1, y1 = start.split(',')
        x1, y1 = int(x1), int(y1)
        x2, y2 = end.split(',')
        x2, y2 = int(x2), int(y2)
        if x1 != x2 and y1 != y2:
            smallx, largex = min(y1, y2), max(y1, y2)
            smally, largey = min(x1, x2), max(x1, x2)
            diffs = largex - smallx
            for diff in range(diffs + 1):
                # had to debug this, did not realize slope mattered
                if (y2 - y1) / (x2 - x1) < 0:
                    new_x = largex - diff
                    new_y = smally + diff
                    points[(new_x, new_y)] += 1
                else:
                    new_x = largex - diff
                    new_y = largey - diff
                    points[(new_x, new_y)] += 1
        elif x1 == x2:
            small, large = min(y1, y2), max(y1, y2)
            for i in range(small, large + 1):
                points[(i, x1)] += 1
        elif y2 == y2:
            small, large = min(x1, x2), max(x1, x2)
            for i in range(small, large + 1):
                points[(y1, i)] += 1

count = 0
for key, value in points.items():
    if value > 1:
        count += 1

print(f'Advent of Code Day 5 Answer Part 2: {count}')

