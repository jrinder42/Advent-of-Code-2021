
"""

Advent of Code 2021 - Day 8

"""

# a rough day

pair = []
with open('day08.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        if not line.strip():
            break
        pair.append(line.split(' | '))

# Part 1

nums = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf',
        5: 'abdfg', 6: 'abdefg', 7: 'acf', 8: 'abcdefg', 9: 'abcdfg'}

nums_len = {}
for key, value in nums.items():
    nums_len[key] = len(value)

unique_nums = [1, 4, 7, 8]

count = 0
for l, r in pair:
    for number in r.split():
        if len(number) in [nums_len[1], nums_len[4], nums_len[7], nums_len[8]]:
            count += 1

print(f'Advent of Code Day 8 Answer Part 1: {count}')

# Part 2

def find_mapping(ll):
    word_map = {}
    for word in sorted(ll, key=lambda x: len(x)):
        # guaranteed
        if len(word) == 2:
            word_map[1] = word
        elif len(word) == 3:
            word_map[7] = word
        elif len(word) == 4:
            word_map[4] = word
        elif len(word) == 7:
            word_map[8] = word

    for word in sorted(ll, key=lambda x: len(x)):
        if len(word) == 5:
            x = set(word).difference(word_map[7])
            y = set(word).difference(word_map[4])
            if len(x) == 2:
                word_map[3] = word
            elif len(y) == 2:
                word_map[5] = word
            else:
                word_map[2] = word
        elif len(word) == 6:
            x = set(word).difference(word_map[5])
            y = set(word).difference(word_map[7])
            if len(x) == 1 and len(y) == 4:
                word_map[6] = word
            elif len(y) == 3 and len(x) == 1:
                word_map[9] = word
            else:
                word_map[0] = word

    return word_map

count = 0
for p in pair:
    l = p[0].split()
    r = p[1].split()
    wm = find_mapping(l)
    rev = {}
    for key, value in wm.items():
        value = ''.join(sorted(value))
        rev[value] = key
    s = ''
    for word in r:
        word = ''.join(sorted(word))
        number = rev[word]
        s += f'{number}'
    count += int(s)

print(f'Advent of Code Day 8 Answer Part 2: {count}')





