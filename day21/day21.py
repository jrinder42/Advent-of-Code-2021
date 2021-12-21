
"""

Advent of Code 2021 - Day 21

"""

from functools import lru_cache
from itertools import product
from queue import Queue

filename = 'day21.txt'

p1, p2 = 0, 0
with open(filename, 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        if not p1:
            p1 = line.split(':')[1].strip()
            p1 = int(p1)
        else:
            p2 = line.split(':')[1].strip()
            p2 = int(p2)

# Part 1

p1_score, p2_score = 0, 0
die = Queue()
for i in range(1, 100 + 1):
    die.put(i)

turn = 0  # 0 for p1, 1 for p2
rolled = 0
while p1_score < 1000 and p2_score < 1000:
    roll_total = 0
    for i in range(3):
        roll = die.get()
        roll_total += roll
        die.put(roll)
        rolled += 1

    if not turn:  # p1
        new_position = (p1 + roll_total) % 10
        if not new_position:
            new_position = 10
        p1 = new_position
        p1_score += p1
        turn = 1
    else:  # p2
        new_position = (p2 + roll_total) % 10
        if not new_position:
            new_position = 10
        p2 = new_position
        p2_score += p2
        turn = 0

pa = 0
if p1_score < p2_score:
    pa = p1_score * rolled
else:
    pa = p2_score * rolled

print(f'Advent of Code Day 21 Answer Part 1: {pa}')

# Part 2

p1, p2 = 0, 0
with open(filename, 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        if not p1:
            p1 = line.split(':')[1].strip()
            p1 = int(p1)
        else:
            p2 = line.split(':')[1].strip()
            p2 = int(p2)

@lru_cache(maxsize=None)
def play(ps, p_score=None, turn=0):
    if p_score is None:
        p_score = (0, 0)

    p1, p2 = ps
    p1_score, p2_score = p_score
    wins = [0, 0]
    die_range = range(1, 3 + 1)
    # new_position
    for i, j, k in product(*[die_range, die_range, die_range]):
        roll_total = i + j + k
        if not turn:  # p1
            new_p1_position = (p1 + roll_total) % 10
            if not new_p1_position:
                new_p1_position = 10

            new_p1_score = p1_score + new_p1_position
            if new_p1_score >= 21:
                wins[0] += 1
            else:
                x = play((new_p1_position, p2), (new_p1_score, p2_score), 1)
                wins[0] += x[0]
                wins[1] += x[1]
        else:  # p2
            new_p2_position = (p2 + roll_total) % 10
            if not new_p2_position:
                new_p2_position = 10

            new_p2_score = p2_score + new_p2_position
            if new_p2_score >= 21:
                wins[1] += 1
            else:
                x = play((p1, new_p2_position), (p1_score, new_p2_score), 0)
                wins[0] += x[0]
                wins[1] += x[1]

    return wins

wins = play((p1, p2))

print(f'Advent of Code Day 21 Answer Part 2: {max(wins)}')

