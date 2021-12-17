
"""

Advent of Code 2021 - Day 17

"""

from itertools import product

x_min, x_max = 0, 0
y_min, y_max = 0, 0
with open('day17.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        line = line.split(': ')[1]
        x, y = line.split(', ')
        x_min, x_max = x.split('..')
        x_min = x_min.split('=')[1]
        y_min, y_max = y.split('..')
        y_min = y_min.split('=')[1]
x_min, x_max = int(x_min), int(x_max)
y_min, y_max = int(y_min), int(y_max)

# Part 1 / Part 2

pairs = product(range(x_max + 1), range(y_min, abs(y_min) + 1))
p1 = 0
initial_velocity = set()  # for part 2
for x_velocity, y_velocity in pairs:
    x_init, y_init = 0, 0
    y = [y_init]
    xo = x_velocity
    yo = y_velocity
    while x_init <= x_max and y_init >= y_min:
        x_init += x_velocity
        y_init += y_velocity
        y.append(y_init)

        # check
        if x_min <= x_init <= x_max and y_min <= y_init <= y_max:
            initial_velocity.add((xo, yo))
            if max(y) > p1:
                p1 = max(y)
            break

        if x_velocity > 0:
            x_velocity -= 1

        y_velocity -= 1

print(f'Advent of Code Day 17 Answer Part 1: {p1}')

# Part 2

print(f'Advent of Code Day 17 Answer Part 2: {len(initial_velocity)}')
