
"""

Advent of Code 2021 - Day 20

"""

import time
import numpy as np

first = ''
second = []
gap = False
with open('day20.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        if not line.strip():
            gap = True
            continue

        if not gap:
            first = line
        else:
            second.append([1 if char == '#' else 0 for char in line])

second = np.array(second)

# Part 1

start_time = time.time()

def enhance_step(second, coord, blank=0):
    i, j = coord
    n, m = second.shape
    value_check = ''
    for ii in range(-1, 1 + 1):
        for jj in range(-1, 1 + 1):
            new_i, new_j = i + ii, j + jj
            if not (0 <= new_i < n - 0 and 0 <= new_j < m - 0):
                value_check += f'{blank}'
            else:
                if second[new_i, new_j]:
                    value_check += '1'
                else:
                    value_check += '0'

    return int(value_check, 2)

def enhance(second, steps=2):
    flip_value = first[0]
    for step in range(steps):
        if not step:
            flip = 0
        else:
            flip = 1 if first[flip_value] == '#' else 0

        second = np.pad(second, pad_width=2, constant_values=flip)
        matrix = second.copy()
        for r in range(matrix.shape[0]):
            for c in range(matrix.shape[1]):
                val = enhance_step(second, (r, c), blank=flip)
                lookup = first[val]
                if lookup == '#':
                    matrix[r, c] = 1
                else:
                    matrix[r, c] = 0

        flip_value = str(flip) * 9
        flip_value = int(flip_value, 2)
        second = matrix

    return second

p1 = enhance(second.copy(), steps=2)
print(f'Advent of Code Day 20 Answer Part 1: {p1.sum()}')

# Part 2

p2 = enhance(second.copy(), steps=50)
print(f'Advent of Code Day 20 Answer Part 2: {p2.sum()}')

print(f'Total elapsed time: {time.time() - start_time}')


