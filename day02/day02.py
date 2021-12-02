
"""

Advent of Code 2021 - Day 2

"""

# Part 1

x = 0
y = 0
with open('day02.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        dir, val = line.split()
        if dir == 'forward':
            x += float(val)
        elif dir == 'down':
            y += float(val)
        elif dir == 'up':
            y -= float(val)

print(f'Advent of Code Day 2 Answer Part 1: {x * y}')

# Part 2

x = 0
y = 0
aim = 0
with open('day02.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        dir, val = line.split()
        if dir == 'forward':
            x += float(val)
            y += aim * float(val)  # this got me cus I did "aim * x" :(
        elif dir == 'down':
            aim += float(val)
        elif dir == 'up':
            aim -= float(val)

print(f'Advent of Code Day 2 Answer Part 2: {x * y}')


