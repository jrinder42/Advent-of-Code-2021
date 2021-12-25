
"""

Advent of Code 2021 - Day 25

"""

import time
import numpy as np

sea_cucumbers = []
with open('day25.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        sea_cucumbers.append([char for char in line])

sea_cucumbers = np.array(sea_cucumbers)

start_time = time.time()

n, m = sea_cucumbers.shape
before = sea_cucumbers.copy()
c = 0
while True:
    # check east
    grid = sea_cucumbers.copy()
    for i in range(n):
        for j in range(m):
            if sea_cucumbers[i, j] == '>':
                new_i, new_j = i, (j + 1) % m
                if sea_cucumbers[new_i, new_j] == '.':
                    grid[i, j] = '.'
                    grid[new_i, new_j] = '>'

    sea_cucumbers = grid
    grid = sea_cucumbers.copy()

    # check south
    for i in range(n):
        for j in range(m):
            if sea_cucumbers[i, j] == 'v':
                new_i, new_j = (i + 1) % n, j
                if sea_cucumbers[new_i, new_j] == '.':
                    grid[i, j] = '.'
                    grid[new_i, new_j] = 'v'

    sea_cucumbers = grid

    if np.array_equal(sea_cucumbers, before):
        c += 1
        break

    before = sea_cucumbers
    c += 1

print(f'Advent of Code Day 25 Answer Part 1: {c}')

print(f'Total elapsed time: {time.time() - start_time}')
