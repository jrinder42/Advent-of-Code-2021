
"""

Advent of Code 2021 - Day 10

"""

# should have been relatively easy, but i overthought it

import numpy as np

lines = []
with open('day10.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        lines.append(line)

# Part 1

# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
open_list = ["[", "{", "(", "<"]
close_list = ["]", "}", ")", '>']

# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False, stack, 'corrupted', i  # unbalanced
    if len(stack) == 0:
        return True, stack, '', -1  # balanced
    else:
        return False, stack, 'incomplete', -1  # unbalanced

vals = {')': 3, ']': 57, '}': 1197, '>': 25137}

total = 0
for i, line in enumerate(lines):
    c, s, word, gold = check(line)
    if word == 'corrupted':
        total += vals[gold]

print(f'Advent of Code Day 10 Answer Part 1: {total}')

# Part 2

new_map = {')': 1, ']': 2, '}': 3, '>': 4}
char_map = {'[': ']', '{': '}', '(': ')', '<': '>'}

scores = []
for i, line in enumerate(lines):
    c, s, word, gold = check(line)
    if word == 'incomplete':
        new_word = []
        for char in s:
            new_word.append(char_map[char])
        new_word = ''.join(new_word[::-1])
        total = 0

        for char in new_word:
            total *= 5
            total += new_map[char]
        scores.append(total)

print(f'Advent of Code Day 10 Answer Part 2: {np.median(scores)}')

