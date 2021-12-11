
"""

Advent of Code 2021 - Day 11

"""

from copy import deepcopy

nums = []
with open('day11.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        nums.append([int(num)for num in line])

# from stackoverflow
def get_adjacent_indices(i, j, m, n) -> list:
    adjacent_indices = []
    if i > 0:  # left
        adjacent_indices.append((i - 1, j))
    if i + 1 < m:  # right
        adjacent_indices.append((i + 1, j))
    if j > 0:  # up
        adjacent_indices.append((i, j - 1))
    if j + 1 < n:  # down
        adjacent_indices.append((i, j + 1))
    # diagonal
    if j > 0 and i + 1 < m:  # down left
        adjacent_indices.append((i + 1, j - 1))
    if i > 0 and j > 0:  # up left
        adjacent_indices.append((i - 1, j - 1))
    if i > 0 and j + 1 < n:  # up right
        adjacent_indices.append((i - 1, j + 1))
    if j + 1 < n and i + 1 < m:  # down right
        adjacent_indices.append((i + 1, j + 1))
    return adjacent_indices

m = len(nums)
n = len(nums[0])

def step(i, j, nums=None, has_flashed=None):  # recursive
    cells = get_adjacent_indices(i, j, m, n)
    for x, y in cells:
        if (x, y) not in has_flashed:
            nums[x][y] += 1

    gt = [(x, y) for x, y in cells if nums[x][y] > 9]
    if len(gt) == 0:
        return
    else:
        for x, y in gt:
            if (x, y) not in has_flashed:
                has_flashed.append((x, y))
                nums[x][y] = 0
                step(x, y, nums, has_flashed)

def problem(nums=None):
    octos = []
    for i in range(m):
        for j in range(n):
            nums[i][j] += 1
            if nums[i][j] > 9:
                octos.append((i, j))

    has_flashed = []
    for r, c in octos:
        if (r, c) not in has_flashed:
            has_flashed.append((r, c))
            nums[r][c] = 0
            step(r, c, nums, has_flashed)

    return nums, has_flashed

p1 = deepcopy(nums)
flashed = 0
for i in range(1, 100 + 1):
    p1, f = problem(p1)
    flashed += len(f)

print(f'Advent of Code Day 11 Answer Part 1: {flashed}')

# Part 2

num_steps = 1
found = False
p2 = nums.copy()
while not found:
    p2, f = problem(p2)
    if len(f) == m * n:
        found = True
        continue

    num_steps += 1

print(f'Advent of Code Day 11 Answer Part 2: {num_steps}')

