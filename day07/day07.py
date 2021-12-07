
"""

Advent of Code 2021 - Day 7

"""

nums = []
with open('day07.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        nums += line.split(',')
nums = [int(num) for num in nums]

# Part 1

def fuel(f, nums):
    for i, num in enumerate(nums):
        nums[i] -= f
        if nums[i] < 0:
            nums[i] = abs(nums[i])
    return nums

m = [float('inf'), float('inf')]
for num in set(nums):
    x = nums.copy()
    val = sum(fuel(num, x))
    if val < m[1]:
        m = [num, val]

print(f'Advent of Code Day 7 Answer Part 1: {m[1]}')

# Part 2

def fuel_p2(f, nums):
    vals = []
    for i, num in enumerate(nums):
        if nums[i] > f:
            x = nums[i] - f
            val = x * (x + 1) / 2
            vals.append(val)
        elif nums[i] < f:
            x = f - nums[i]
            val = x * (x + 1) / 2
            vals.append(val)
        else:
            vals.append(0)

    return vals

m = [float('inf'), float('inf')]
for num in range(1, max(nums) + 1):
    x = nums.copy()
    val = sum(fuel_p2(num, x))
    if val < m[1]:
        m = [num, val]

print(f'Advent of Code Day 7 Answer Part 2: {m[1]}')
