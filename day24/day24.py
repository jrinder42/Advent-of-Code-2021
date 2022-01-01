
"""

Advent of Code 2021 - Day 24

"""

instructions = []
with open('day24.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        instructions.append(line.split(' ', 1))

adds = []
add = []
for instruction in instructions:
    name, item = instruction
    if name == 'inp':
        if add:
            adds.append([add[0], add[-1]])
        add = []
    elif name == 'add':
        var, val = item.split()
        if val.strip('-').isnumeric():
            add.append(int(val))
adds.append([add[0], add[-1]])

def valid_monad(monad, adds):
    z = 0
    for i, char in enumerate(monad):
        w = int(char)
        add = adds[i]
        if z % 26 + add[0] == w:
            z //= 26
        else:
            # remainder -- z % 26 = (previous) w + add[1]
            z = z * 26 + (w + add[1])

    return z

def find_valid_monad(monad, adds):
    monad = list(map(int, monad))
    stack = []
    for i in range(len(monad)):
        add = adds[i]
        div = 26 if add[0] < 0 else 1
        if div == 1:
            stack.append((i, add[1]))
        else:
            new_index, new_add = stack.pop()
            monad[i] = monad[new_index] + add[0] + new_add
            if monad[i] > 9:
                monad[new_index] -= monad[i] - 9
                monad[i] = 9
            elif monad[i] < 1:
                monad[new_index] += 1 - monad[i]
                monad[i] = 1

    monad = map(str, monad)
    return ''.join(monad)

p1 = find_valid_monad('9' * 14, adds)
p1 = p1 if valid_monad(p1, adds) == 0 else False

print(f'Advent of Code Day 24 Answer Part 1: {p1}')

p2 = find_valid_monad('1' * 14, adds)
p2 = p2 if valid_monad(p2, adds) == 0 else False

print(f'Advent of Code Day 24 Answer Part 2: {p2}')
