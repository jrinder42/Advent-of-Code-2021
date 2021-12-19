
"""

Advent of Code 2021 - Day 18

"""

import re
from math import floor, ceil
from copy import deepcopy
import time
from itertools import combinations

nums = []
with open('day18.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        nums.append(line)

# Part 1

start_time = time.time()

def split_left(topaz):
    fs = []
    start = 0
    for elem in re.findall('\d+', topaz):
        place = topaz.index(elem, start)
        start = place + len(elem)
        fs.append((place, elem))
    return fs

def is_balanced(topaz):  # for debugging only
    oo = []
    for elem in topaz:
        if elem == '[':
            oo.append(elem)
        elif elem == ']':
            oo.pop()
    return not oo

def add_elements(one, two):
    return f'[{one},{two}]'

def reduce(topaz):
    has_exploded = []
    explode = False
    split = False
    indx = 0
    topaz = deepcopy(topaz)
    opening = []
    while indx < len(topaz):
        char = topaz[indx]

        if char.isnumeric() and not explode and len(opening) < 5:
            fs = ()
            start = 0
            for elem in re.findall(r'\d+', topaz[:indx + 1]):
                place = topaz.index(elem, start)
                start = place + 1
                fs = (place, int(elem))  # (index, number)
            if fs[-1] > 9:
                length = len(str(fs[-1]))  # should always be 2
                l = floor(fs[-1] / 2)
                r = ceil(fs[-1] / 2)
                topaz = f'{topaz[:fs[0]]}[{l},{r}]{topaz[fs[0] + length:]}'

                opening = []
                explode = False
                split = False
                indx = -1

            indx += 1

        elif char == '[':
            opening.append((indx, char))
            indx += 1
        elif char == ']':
            new_o = opening.pop()
            o_index = new_o[0]
            c_index = indx + 1
            e = eval(topaz[o_index:c_index])
            if has_exploded:
                if str(e).count('[') == 1 and str(e).count(']') == 1:
                    indx += 1
                    continue

                if isinstance(e[0], int):
                    e[0] += e[1][0]
                    # check if there is a number to the right
                    right_numbers = re.findall(r'\d+', topaz[c_index:])
                    if right_numbers:
                        right = e[1][1] + int(right_numbers[0])
                        right_index = topaz[c_index:].find(right_numbers[0])
                        val = len(str(right_numbers[0]))

                        topaz = f'{topaz[:c_index + right_index]}' \
                                f'{right}' \
                                f'{topaz[c_index + right_index + val:]}'

                    e[1] = 0
                    e = ''.join([val for val in str(e) if val.strip()])

                    # modify string to reflect this new e
                    topaz = f'{topaz[:o_index]}{e}{topaz[c_index:]}'
                elif isinstance(e[1], int):  # isinstance(e[0], list)
                    e[1] += e[0][1]
                    # check if there is a number to the right
                    left_numbers = re.findall(r'\d+', topaz[:o_index])
                    if left_numbers:
                        left = int(left_numbers[-1]) + e[0][0]
                        left_index = split_left(topaz[:o_index])[-1][0]
                        val = len(str(left_numbers[-1]))

                        topaz = f'{topaz[:left_index]}' \
                                f'{left}' \
                                f'{topaz[left_index + val:]}'

                        diff = len(str(left)) - len(str(left_numbers[-1]))
                        o_index += diff
                        c_index += diff

                    e[0] = 0
                    e = ''.join([val for val in str(e) if val.strip()])

                    # modify string to reflect this new e
                    topaz = f'{topaz[:o_index]}{e}{topaz[c_index:]}'
                else:  # (list, list)
                    e[1][0] += e[0][1]
                    # check if there is a number to the right
                    left_numbers = re.findall(r'\d+', topaz[:o_index])
                    if left_numbers:
                        left = int(left_numbers[-1]) + e[0][0]
                        left_index = split_left(topaz[:o_index])[-1][0]
                        val = len(str(left_numbers[-1]))

                        topaz = f'{topaz[:left_index]}' \
                                f'{left}' \
                                f'{topaz[left_index + val:]}'

                        diff = len(str(left)) - len(str(left_numbers[-1]))
                        o_index += diff
                        c_index += diff

                    e[0] = 0
                    e = ''.join([val for val in str(e) if val.strip()])

                    # modify string to reflect this new e
                    topaz = f'{topaz[:o_index]}{e}{topaz[c_index:]}'

                has_exploded = []
                opening = []
                indx = -1
                explode = True

                # for debugging
                if not is_balanced(topaz):
                    print(f'topaz is not balanced: {topaz}')
                    exit(5)
            elif len(opening) + 1 > 4:  # explosion
                has_exploded = (e, indx)
                explode = True

            indx += 1
        else:
            indx += 1

        if len(topaz) <= indx and (explode or split):
            indx = 0
            opening = []
            explode = False
            split = False

    return topaz

problem = nums[0]
for snailfish in nums[1:]:
    problem = add_elements(problem, snailfish)
    problem = reduce(problem)

def find_magnitude(topaz):
    topaz = deepcopy(topaz)
    indx = 0
    opening = []
    while not topaz.isnumeric():
        char = topaz[indx]
        if char == '[':
            opening.append((indx, char))
            indx += 1
        elif char == ']':
            new_o = opening.pop()
            o_index = new_o[0]
            c_index = indx + 1
            e = eval(topaz[o_index:c_index])
            l, r = e
            number = 3 * l + 2 * r
            topaz = f'{topaz[:o_index]}{number}{topaz[c_index:]}'
            indx = o_index + 1
        else:
            indx += 1

    return int(topaz)

print(f'Advent of Code Day 18 Answer Part 1: {find_magnitude(problem)}')

# Part 2

combos = combinations(nums, 2)
m = [0, '']
for x, y in combos:
    pair1 = add_elements(x, y)
    pair2 = add_elements(y, x)

    pair1 = reduce(pair1)
    pair2 = reduce(pair2)

    pair1_value = find_magnitude(pair1)
    pair2_value = find_magnitude(pair2)

    if pair1_value > m[0]:
        m = [pair1_value, pair1]

    if pair2_value > m[0]:
        m = [pair2_value, pair2]

print(f'Advent of Code Day 18 Answer Part 2: {m[0]}')

print(f'Total elapsed time: {time.time() - start_time}')

