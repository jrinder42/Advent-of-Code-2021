
"""

Advent of Code 2021 - Day 13

"""

# This along with any matrix solution is not a general solution

import numpy as np

nums = []
switch = False
max_x, max_y = 0, 0
folds = []
with open('day13.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        if not line.strip():
            switch = True
            continue

        if not switch:
            l, r = line.split(',')  # x, y
            l, r = int(l), int(r)
            nums.append((r, l))
            if l > max_x:
                max_x = l
            if r > max_y:
                max_y = r
        else:
            vals = line.rsplit(' ', 1)[1]
            dir, val = vals.split('=')
            folds.append((dir, int(val)))

arr = np.zeros((max_y + 1, max_x + 1))
for i, j in nums:
    arr[i, j] = 1

# Part 1

p1 = 0
for i, (char, num) in enumerate(folds):
    # assumes even matrices are at most 1-off
    if char == 'y':
        flip = np.flipud(arr)[:num, :]
        if arr.shape[0] % 2 == 0:
            flip = np.roll(flip, 1, axis=0)
            flip[0, :] = 0
        arr = arr[:num, :]
    else:
        flip = np.fliplr(arr)[:, :num]
        if arr.shape[1] % 2 == 0:
            flip = np.roll(flip, 1, axis=1)
            flip[:, 0] = 0
        arr = arr[:, :num]

    arr = np.add(arr, flip)
    arr[arr > 1] = 1

    if i == 0:
        p1 = arr.sum()

print(f'Advent of Code Day 13 Answer Part 1: {p1}')

# Part 2

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print('#' if arr[i, j] == 1 else ' ', end='')
    print('')

p2 = 'FJAHJGAH'
print(f'Advent of Code Day 13 Answer Part 2: {p2}')