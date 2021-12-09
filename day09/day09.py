
"""

Advent of Code 2021 - Day 9

"""

from collections import defaultdict

import numpy as np

nums = []
with open('day09.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        nums.append([int(char) for char in line])

nums = np.array(nums)

# from stackoverflow
def get_adjacent_indices(i, j, m, n) -> list:
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i - 1, j))
    if i + 1 < m:
        adjacent_indices.append((i + 1, j))
    if j > 0:
        adjacent_indices.append((i, j - 1))
    if j + 1 < n:
        adjacent_indices.append((i, j + 1))
    return adjacent_indices

candidate = []
ci = []
for i in range(nums.shape[0]):
    for j in range(nums.shape[1]):
        # list of tuples (i, j)
        cells = get_adjacent_indices(i, j, nums.shape[0], nums.shape[1])
        count = 0
        for x, y in cells:
            if nums[i, j] < nums[x, y]:
                count += 1
        if count == len(cells):
            candidate.append(nums[i, j] + 1)
            ci.append((i, j))

print(f'Advent of Code Day 9 Answer Part 1: {sum(candidate)}')

# Part 2

basin = defaultdict(list)  # keys are ci elements

for i in range(nums.shape[0]):
    for j in range(nums.shape[1]):
        # start recursion...but I don't use recursion
        new_i, new_j = i, j
        lst = set()
        while (new_i, new_j) not in ci:
            m = [9, ()]
            cells = get_adjacent_indices(new_i, new_j, nums.shape[0], nums.shape[1])
            for x, y in cells:
                if nums[x, y] < m[0]:
                    m = (nums[x, y], (x, y))

            if nums[new_i, new_j] != 9:
                lst.add((new_i, new_j))
            if not m[1]:
                break
            new_i, new_j = m[1][0], m[1][1]
        if nums[new_i, new_j] != 9:
            lst.add((new_i, new_j))

        # did this because i was having trouble with defaultdict(set)
        basin[(new_i, new_j)] += lst
        basin[(new_i, new_j)] = list(set(basin[(new_i, new_j)]))


basin_lens = {}
basin_values = defaultdict(list)
for key, value in basin.items():
    basin_lens[key] = len(value)
    for x, y in value:
        basin_values[key].append(nums[x, y])
basin_lens = {k: v for k, v in sorted(basin_lens.items(),
                                      key=lambda item: item[1],
                                      reverse=True)}

count = 0
mult = 1
for key, value in basin_lens.items():
    mult *= value
    count += 1
    if count == 3:
        break

print(f'Advent of Code Day 9 Answer Part 2: {mult}')