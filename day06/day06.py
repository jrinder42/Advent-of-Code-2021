
"""

Advent of Code 2021 - Day 6

"""

from collections import Counter

nums = []
with open('day06.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        nums += line.split(',')
nums = [int(num) for num in nums]

# Part 1

def num_fish(nums=None, days=18):
    for day in range(days):
        to_add = []
        for i, num in enumerate(nums):
            if num == 0:
                nums[i] = 6
                to_add.append(8)
            else:
                nums[i] -= 1
        nums += to_add

    return nums

x = num_fish(nums=nums.copy(), days=80)

print(f'Advent of Code Day 6 Answer Part 1: {len(x)}')

# Part 2

# part 1 is too slow, but probs could have worked in something like C++ or Rust
# part 1 is too slow for part 2, took me forever to find a new solution

def num_fish_v2(nums=None, days=18):
    c = Counter(nums)
    q = set(range(9))
    for day in range(1, days + 1):
        new = c.copy()
        diff = q.difference(c.keys())
        for key in sorted(c.keys()):
            value = c[key]
            if key == 0:
                val = value
                new[6] = val
                new[8] = val
            else:
                c[key - 1] = value
        c[6] += new[6]
        c[8] = new[8]
        for d in diff:
            if d == 0:
                continue
            c[d - 1] = 0

    return c

x = num_fish_v2(nums=nums, days=256)

print(f'Advent of Code Day 6 Answer Part 2: {sum(x.values())}')


