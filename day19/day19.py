
"""

Advent of Code 2021 - Day 19

"""

from collections import defaultdict
from itertools import combinations, product
import re
import time
from math import sqrt
import numpy as np

scanners = defaultdict(list)
val = 0
with open('day19.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        if not line.strip():
            continue

        if 'scanner' in line:
            val = int(re.findall(r'\d+', line)[0])
        else:
            scanners[val].append(list(map(int, line.split(','))))

# Part 1

start_time = time.time()

def calculate_distance(scanner):
    zero = []
    zero_values = []
    for pair1, pair2 in combinations(scanners[scanner], 2):
        val = 0
        for i in range(3):  # x, y, z
            val += (pair1[i] - pair2[i]) ** 2

        distance = sqrt(val)  # euclidean distance
        if distance not in zero:
            zero.append(distance)
            zero_values.append((tuple(pair1), tuple(pair2)))  # for beacons

    return zero, zero_values

def rotate(p, rotation):
    x, y, z = p
    if rotation == 0:
        return (x, y, z)
    if rotation == 1:
        return (x, -z, y)
    if rotation == 2:
        return (x, -y, -z)
    if rotation == 3:
        return (x, z, -y)
    if rotation == 4:
        return (-x, -y, z)
    if rotation == 5:
        return (-x, -z, -y)
    if rotation == 6:
        return (-x, y, -z)
    if rotation == 7:
        return (-x, z, y)
    if rotation == 8:
        return (y, x, -z)
    if rotation == 9:
        return (y, -x, z)
    if rotation == 10:
        return (y, z, x)
    if rotation == 11:
        return (y, -z, -x)
    if rotation == 12:
        return (-y, x, z)
    if rotation == 13:
        return (-y, -x, -z)
    if rotation == 14:
        return (-y, -z, x)
    if rotation == 15:
        return (-y, z, -x)
    if rotation == 16:
        return (z, x, y)
    if rotation == 17:
        return (z, -x, -y)
    if rotation == 18:
        return (z, -y, x)
    if rotation == 19:
        return (z, y, -x)
    if rotation == 20:
        return (-z, x, -y)
    if rotation == 21:
        return (-z, -x, y)
    if rotation == 22:
        return (-z, y, x)
    if rotation == 23:
        return (-z, -y, -x)
    return ()

def find_alignment(v1, v2):
    for align in range(4 * 6):
        new_v2 = rotate(v2, align)
        if np.cross(v1, new_v2).sum() == 0:
            return align

    return False

def beacons(scanner1, scanner2):
    zero, zero_values = calculate_distance(scanner1)
    one, one_values = calculate_distance(scanner2)

    unique_beacons = set()
    beacon_scanners = defaultdict(list)
    for i, elem in enumerate(zero):
        if elem in one:  # if the distance is in both sets
            indx = one.index(elem)

            unique_beacons.add(zero_values[i][0])
            unique_beacons.add(zero_values[i][1])

            beacon_scanners[zero_values[i][0]].append((zero_values[i],
                                                       one_values[indx]))
            beacon_scanners[zero_values[i][1]].append((zero_values[i],
                                                       one_values[indx]))

    if len(unique_beacons) < 12:
        return (), (), -1

    # get coordinates that appear more than once
    beacon_map = {}
    beacon_pos = ()
    pear = ()
    fr = -1
    for beacon, value in beacon_scanners.items():
        if len(value) > 1:
            # a pair is comprised of 2 tuples, each with 2 tuples
            pair1 = value[0]
            pair2 = value[1]
            # left is in zero, right is in one -- these are 2 sets of tuples
            p1_left, p1_right = pair1
            p2_left, p2_right = pair2
            if p1_right[0] in p2_right:
                common = p1_right[0]
                common_index = 0
            else:
                common = p1_right[1]
                common_index = 1
            beacon_index = p1_left.index(beacon)

            map1 = (beacon, common)
            map2 = (p1_left[(beacon_index + 1) % 2],
                    p1_right[(common_index + 1) % 2])

            beacon_map[map1[0]] = map1[1]
            beacon_map[map2[0]] = map2[1]

            vec1 = []
            vec2 = []
            for pos in range(3):
                vec1.append(map1[0][pos] - map2[0][pos])  # < 0)
                vec2.append(map1[1][pos] - map2[1][pos])  # < 0)

            fr = find_alignment(vec1, vec2)
            if isinstance(fr, int):
                p1 = rotate(map1[1], fr)
                p2 = rotate(map2[1], fr)
                diff = np.array(map1[0]) - np.array(p1)
                beacon_pos = diff
                pear = map1
                return beacon_pos, pear, fr
            else:
                continue

    return beacon_pos, pear, fr

potential = list(scanners.keys())
potential.remove(0)
vals = {}
while potential:
    for s1, s2 in product(scanners.keys(), scanners.keys()):
        if s1 == s2:
            continue

        bp, pear, align = beacons(s1, s2)
        zero = s1 == 0 and s2 in vals or s2 == 0 and s1 in vals
        if len(bp) == 0 or zero:
            continue

        if s1 == 0 and len(bp) > 0:
            vals[s2] = bp, align
            potential.remove(s2)
        elif s1 > 0 and s1 in vals and s2 not in vals and s2 > 0:
            x = np.array(rotate(pear[1], align))
            x = np.array(rotate(x, vals[s1][1]))
            new_align = align
            for a in range(24):
                if all(x == rotate(pear[1], a)):
                    new_align = a
                    break

            y = np.array(rotate(pear[0], vals[s1][1]))
            y += np.array(vals[s1][0])
            vals[s2] = (y - x), new_align
            potential.remove(s2)

        if not potential:
            break

final = set()
for elem in scanners[0]:
    final.add(tuple(elem))

for scanner, pair in vals.items():
    base, location = pair
    for beacon in scanners[scanner]:
        v = np.array(rotate(beacon, location))
        v += np.array(base)
        final.add(tuple(v))

print(f'Advent of Code Day 19 Answer Part 1: {len(final)}')

# Part 2

def manhattan(beacon1, beacon2):
    total = 0
    for i in range(3):
        total += abs(beacon1[i] - beacon2[i])
    return total

m = [0, ()]
for k1, k2 in product(vals.keys(), vals.keys()):
    if k1 == k2:
        continue

    distance = manhattan(vals[k1][0], vals[k2][0])
    if distance > m[0]:
        m = [distance, (vals[k1][0], vals[k2][0])]

print(f'Advent of Code Day 19 Answer Part 2: {m[0]}')

print(f'Total elapsed time: {time.time() - start_time}')

