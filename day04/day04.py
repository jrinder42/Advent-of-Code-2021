
"""

Advent of Code 2021 - Day 4

"""

import numpy as np

boards = []
nums = []
b = []
with open('day04.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        if i == 0:
            nums = list(map(int, line.split(',')))
        else:
            if line.strip():
                x = list(map(int, line.split()))
                b.append(x)
            else:
                if b:
                    boards.append(np.array(b))
                    b = []
boards.append(np.array(b))

def win(board, numbers):
    for i in range(board.shape[0]):
        row = 0
        for elem in board[i, :]:
            if elem in numbers:
                row += 1
        if row == board.shape[1]:
            return True

    for j in range(board.shape[1]):
        col = 0
        for elem in board[:, j]:
            if elem in numbers:
                col += 1
        if col == board.shape[0]:
            return 1

    return False

# Part 1

to_break = False
unmarked = 0
n = 0
for i in range(len(nums)):
    if to_break:
        break
    for board in boards:
        has_won = win(board, nums[:i])
        if has_won:
            for w in range(board.shape[0]):
                for z in range(board.shape[1]):
                    if board[w, z] not in nums[:i]:
                        unmarked += board[w, z]

            n = nums[i - 1]
            to_break = True
            break

print(f'Advent of Code Day 4 Answer Part 1: {unmarked * n}')

# Part 2

octo_set = set()

to_break = False
unmarked = 0
n = 0
for i, num in enumerate(nums):
    if to_break:
        break
    for check, board in enumerate(boards):
        has_won = win(board, nums[:i])
        if has_won:
            if check not in octo_set and len(octo_set) == len(boards) - 1:
                for w in range(board.shape[0]):
                    for z in range(board.shape[1]):
                        if board[w, z] not in nums[:i]:
                            unmarked += board[w, z]

                n = nums[i - 1]
                to_break = True
                break
            else:
                octo_set.add(check)

print(f'Advent of Code Day 4 Answer Part 2: {unmarked * n}')

