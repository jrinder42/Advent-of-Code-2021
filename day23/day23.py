
"""

Advent of Code 2021 - Day 23

"""

import heapq
from itertools import product
import time
import numpy as np

n = 0
grid = []
with open('day23.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        grid.append([char for char in line])
        if i == 0:
            n = len(grid[0])

for i, row in enumerate(grid):
    if len(row) < n:
        # pad the grid
        row = [char for char in row if char.strip()]
        grid[i] = ['#', '#'] + row + ['#', '#']

# Part 1

start_time = time.time()

grid = np.array(grid)

target_grid = grid.copy()
target_grid[2:4, 3] = 'A'
target_grid[2:4, 5] = 'B'
target_grid[2:4, 7] = 'C'
target_grid[2:4, 9] = 'D'

def to_buffer(x):
    return x.tobytes()

def from_buffer(x, grid):
    return np.frombuffer(x, dtype=grid.dtype).reshape(grid.shape)


energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

goals = {'A': [(2, 3), (3, 3)], 'B': [(2, 5), (3, 5)],
         'C': [(2, 7), (3, 7)], 'D': [(2, 9), (3, 9)]}

def find_letter(grid, letter='A'):  # A, B, C, D
    found = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == letter:
                found.append((i, j))

    return found

def make_move(grid, to, at, letter='A'):
    grid[at] = '.'
    grid[to] = letter
    return grid

def find_moves(grid, pair):
    row, col = pair
    letter = grid[row, col]
    goal_col = goals[letter][0][1]
    moves = []
    move_dict = {}
    cost = energy[letter]
    # hallway
    if row == 1:
        if col < goal_col:
            # have to move right
            hallway_moves = grid[row, col + 1:goal_col + 1]
            empty_grid = np.all(hallway_moves == '.')
        else:  # col > goal_col
            # have to move left
            hallway_moves = grid[row, goal_col:col]
            empty_grid = np.all(hallway_moves == '.')

        potential_moves = 0
        empty_moves = []
        move_costs = 0
        for letter_pair in goals[letter]:
            if grid[letter_pair] in ['.', letter]:
                potential_moves += 1
                if grid[letter_pair] == '.':
                    empty_move = not empty_moves
                    full_move = empty_moves and letter_pair[0] > empty_moves[0]
                    if empty_move or full_move:
                        empty_moves = letter_pair
                        move_costs = cost * len(hallway_moves)
                        move_costs += cost * (letter_pair[0] - 1)
        can_move = potential_moves == len(goals[letter])
        if empty_grid and can_move:
            moves += empty_moves
            return [(tuple(moves), move_costs)]

        return None

    # not in a hallway
    elif row > 1:
        move_costs = []
        # if the piece cannot move
        if grid[row - 1, col] != '.':
            return None

        # can move out
        # if the piece is already in its final spot
        if col == goal_col:
            col_check = 0
            for letter_pair in product(range(2, grid.shape[0] - 1), [goal_col]):
                if grid[letter_pair] in ['.', letter]:
                    col_check += 1
            col_check = col_check == grid.shape[0] - 2 - 1

            # get the top piece in a row that can move
            start_row = grid.shape[0] - 2
            letter_pair = (start_row, col)
            while grid[letter_pair] == letter:
                start_row -= 1
                letter_pair = (start_row, goal_col)

            letter_pair = (letter_pair[0] + 1, letter_pair[1])
            # if a piece is already at its destination
            if letter_pair == pair and col_check:
                return None
            else:
                # left
                current_cost = cost * (row - 1) - cost
                for elem in product([1], range(col, 0, -1)):
                    current_cost += cost
                    if elem[1] in [3, 5, 7, 9]:
                        continue

                    if grid[elem] == '.':
                        moves.append(elem)
                        move_costs.append(current_cost)
                        move_dict[elem] = current_cost
                    else:
                        break

                # right
                current_cost = cost * (row - 1) - cost
                for elem in product([1], range(col, grid.shape[1] - 1)):
                    current_cost += cost
                    if elem[1] in [3, 5, 7, 9]:
                        continue

                    if grid[elem] == '.':
                        moves.append(elem)
                        move_costs.append(current_cost)
                        move_dict[elem] = current_cost
                    else:
                        break

                return [(k, v) for k, v in move_dict.items()]

        else:
            # get the top piece in a row that can move'
            # check for u turn
            if col < goal_col:
                hallway_moves = grid[1, col:goal_col + 1]
                hallway_bool = np.all(hallway_moves == '.')
            else:
                hallway_moves = grid[1, goal_col:col + 1]
                hallway_bool = np.all(hallway_moves == '.')

            col_count = 0
            for elem in product(range(2, grid.shape[0] - 1), [goal_col]):
                if grid[elem] in ['.', letter]:
                    col_count += 1

            # can do u turn
            if hallway_bool and col_count:
                start_row = grid.shape[0] - 2
                letter_pair = (start_row, goal_col)
                while grid[letter_pair] in goals:
                    start_row -= 1
                    letter_pair = (start_row, goal_col)

                moves.append(letter_pair)
                current_cost = cost * (row - 1)
                current_cost += abs(col - goal_col) * cost
                current_cost += cost * (letter_pair[0] - 1)
                move_costs.append(current_cost)
                move_dict[letter_pair] = current_cost

            # left
            current_cost = cost * (row - 1) - cost
            for elem in product([1], range(col, 0, -1)):
                current_cost += cost
                if elem[1] in [3, 5, 7, 9]:
                    continue

                if grid[elem] == '.':
                    moves.append(elem)
                    move_costs.append(current_cost)
                    move_dict[elem] = current_cost
                else:
                    break

            # right
            current_cost = cost * (row - 1) - cost
            for elem in product([1], range(col, grid.shape[1] - 1)):
                current_cost += cost
                if elem[1] in [3, 5, 7, 9]:
                    continue

                if grid[elem] == '.':
                    moves.append(elem)
                    move_costs.append(current_cost)
                    move_dict[elem] = current_cost
                else:
                    break

            return [(k, v) for k, v in move_dict.items()]

    return None

def generate_moves(grid):
    all_grids = []
    for letter in ['A', 'B', 'C', 'D']:
        letter_positions = find_letter(grid, letter=letter)
        for letter_position in letter_positions:
            x = find_moves(grid, letter_position)
            if x is not None:
                for elem, c in x:
                    g = grid.copy()
                    g = make_move(g, elem, letter_position, letter)
                    all_grids.append((g, c))
    return all_grids

def dijkstra(source, target=None):
    dist = {to_buffer(source): 0}
    if len(target) > 0:
        target = to_buffer(target)
    prev = {}

    hq = []
    heapq.heappush(hq, (dist[to_buffer(source)], to_buffer(source)))

    while hq:
        current_weight, current_state = heapq.heappop(hq)
        if target and current_state == target:
            return dist[current_state]

        for new_state, new_weight in generate_moves(
                from_buffer(current_state, source)):
            new_state = to_buffer(new_state)
            new_weight += current_weight
            if new_state not in dist or new_weight < dist[new_state]:
                dist[new_state] = new_weight
                prev[new_state] = current_state
                heapq.heappush(hq, (new_weight, new_state))

d = dijkstra(grid, target_grid)

print(f'Advent of Code Day 23 Answer Part 1: {d}')

print(f'Total elapsed time - p1: {time.time() - start_time}')

# Part 2

new_piece = [['#', '#', '#', 'D', '#', 'C', '#', 'B', '#', 'A', '#', '#', '#'],
             ['#', '#', '#', 'D', '#', 'B', '#', 'A', '#', 'C', '#', '#', '#']]

new_grid = grid[:3, :]
for elem in new_piece:
    new_grid = np.vstack([new_grid, elem])

new_grid = np.vstack([new_grid, grid[3:]])

new_target_grid = new_grid.copy()
new_target_grid[2:6, 3] = 'A'
new_target_grid[2:6, 5] = 'B'
new_target_grid[2:6, 7] = 'C'
new_target_grid[2:6, 9] = 'D'

d = dijkstra(new_grid, new_target_grid)

print(f'Advent of Code Day 23 Answer Part 2: {d}')

print(f'Total elapsed time - p2: {time.time() - start_time}')


