
"""

Advent of Code 2021 - Day 22

"""

import time
from itertools import product

instructions = []
with open('day22.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        flip, directions = line.split(' ', 1)
        flip = 1 if flip == 'on' else 0
        x, y, z = directions.split(',')
        x = x.split('=')[1].split('..')
        x = range(int(x[0]), int(x[1]) + 1)
        y = y.split('=')[1].split('..')
        y = range(int(y[0]), int(y[1]) + 1)
        z = z.split('=')[1].split('..')
        z = range(int(z[0]), int(z[1]) + 1)
        instructions.append({'flip': flip,
                             'x': x,
                             'y': y,
                             'z': z})

# Part 1

start_time = time.time()
cubes = {}
for ii, instruction in enumerate(instructions):
    flip = instruction['flip']
    x, y, z = instruction['x'], instruction['y'], instruction['z']
    x_min, x_max = min(x), max(x)
    y_min, y_max = min(y), max(y)
    z_min, z_max = min(z), max(z)
    x_bounds = -50 <= x_min <= 50 and -50 <= x_max <= 50
    y_bounds = -50 <= y_min <= 50 and -50 <= y_max <= 50
    z_bounds = -50 <= z_min <= 50 and -50 <= z_max <= 50
    if x_bounds and y_bounds and z_bounds:
        for i, j, k in product(*[x, y, z]):
            cubes[(i, j, k)] = flip

print(f'Advent of Code Day 22 Answer Part 1: {sum(cubes.values())}')

# Part 2

def cube_volume(cube):
    lx = len(range(cube[0], cube[1] + 1))
    ly = len(range(cube[2], cube[3] + 1))
    lz = len(range(cube[4], cube[5] + 1))
    return lx * ly * lz

def find_intersection(base_cube, target_cube):
    edge_geometry = []  # rectangular prisms
    # x edges
    if base_cube[0] < target_cube[0]:
        cube = [base_cube[0], target_cube[0] - 1,
                base_cube[2], base_cube[3],
                base_cube[4], base_cube[5],
                base_cube[6]]
        base_cube[0] = target_cube[0]
        edge_geometry.append(cube)

    if target_cube[1] < base_cube[1]:
        cube = [target_cube[1] + 1, base_cube[1],
                base_cube[2], base_cube[3],
                base_cube[4], base_cube[5],
                base_cube[6]]
        base_cube[1] = target_cube[1]
        edge_geometry.append(cube)

    # y edges
    if base_cube[2] < target_cube[2]:
        cube = [base_cube[0], base_cube[1],
                base_cube[2], target_cube[2] - 1,
                base_cube[4], base_cube[5],
                base_cube[6]]
        base_cube[2] = target_cube[2]
        edge_geometry.append(cube)

    if target_cube[3] < base_cube[3]:
        cube = [base_cube[0], base_cube[1],
                target_cube[3] + 1, base_cube[3],
                base_cube[4], base_cube[5],
                base_cube[6]]
        base_cube[3] = target_cube[3]
        edge_geometry.append(cube)

    # z edges
    if base_cube[4] < target_cube[4]:
        cube = [base_cube[0], base_cube[1],
                base_cube[2], base_cube[3],
                base_cube[4], target_cube[4] - 1,
                base_cube[6]]
        base_cube[4] = target_cube[4]
        edge_geometry.append(cube)

    if target_cube[5] < base_cube[5]:
        cube = [base_cube[0], base_cube[1],
                base_cube[2], base_cube[3],
                target_cube[5] + 1, base_cube[5],
                base_cube[6]]
        base_cube[5] = target_cube[5]
        edge_geometry.append(cube)

    return edge_geometry

on_count = 0
cubes = []  # (x, x), (y, y), (z, z), flip -- 0 or 1
for i, instruction in enumerate(instructions):
    flip = instruction['flip']
    x, y, z = instruction['x'], instruction['y'], instruction['z']
    x_bounds = min(x), max(x)
    y_bounds = min(y), max(y)
    z_bounds = min(z), max(z)
    current_cube = [x_bounds[0], x_bounds[1],
                    y_bounds[0], y_bounds[1],
                    z_bounds[0], z_bounds[1],
                    flip]

    new_cubes = [current_cube]
    for cube in cubes:
        x_inter = x_bounds[0] <= cube[1] and x_bounds[1] >= cube[0]
        y_inter = y_bounds[0] <= cube[3] and y_bounds[1] >= cube[2]
        z_inter = z_bounds[0] <= cube[5] and z_bounds[1] >= cube[4]

        if x_inter and y_inter and z_inter:
            # intersection
            new_cubes += find_intersection(cube, current_cube)
        else:
            new_cubes.append(cube)

    cubes = new_cubes

on_count = 0
for cube in cubes:
    flip = cube[-1]
    if flip:
        on_count += cube_volume(cube)

print(f'Advent of Code Day 22 Answer Part 2: {on_count}')

print(f'Total elapsed time: {time.time() - start_time}')



