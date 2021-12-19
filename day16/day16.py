
"""

Advent of Code 2021 - Day 16

"""

# numpy C-style type issue tool me a while to figure out

from functools import reduce
from operator import mul

num = ''
with open('day16.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        num = line

# Part 1 / Part 2

def get_bin(num):
    b = bin(int(num, 16))
    b = b.split('b')[1]
    c = 0
    while num[c] == '0':
        b = '0000' + b
        c += 1

    while len(b) % 4 > 0:
        b = '0' + b

    return b

def header(num, start):
    # version, id
    return num[start:start + 3], num[start + 3:start + 6]

def find_end(num, start):
    val = num[start:start + 5]
    new_val = val[1:]
    while val[0] != '0':
        start += 5
        val = num[start:start + 5]
        new_val += val[1:]

    return start + 5, int(new_val, 2)

def expression_value(packets, id=0):  # for part 2
    if id == 0:
        return sum(packets)
    elif id == 1:
        # numpy np.prod causes an issue due to C-style types
        return reduce(mul, packets, 1)
    elif id == 2:
        return min(packets)
    elif id == 3:
        return max(packets)
    elif id == 5:
        return 1 if packets[0] > packets[1] else 0
    elif id == 6:
        return 1 if packets[0] < packets[1] else 0
    elif id == 7:
        return 1 if packets[0] == packets[1] else 0

def decode(num, start, v=None):
    if v is None:
        v = []

    version, id = header(b, start)
    version = int(version, 2)
    id = int(id, 2)

    v.append(version)
    start += 6

    if id == 4:
        start, packet_value = find_end(b, start)
        return start, v, packet_value

    packets = []
    if num[start] == '0':
        start += 1
        bit_length = int(num[start:start + 15], 2)  # sub-packets
        start += 15
        original_start = start
        while start != original_start + bit_length:
            start, v, packet_value = decode(num, start, v=v)
            packets.append(packet_value)
    else:  # num[start] == '1'
        start += 1
        num_subpackets = int(num[start:start + 11], 2)  # sub-packets
        start += 11
        for subpacket in range(num_subpackets):
            start, v, packet_value = decode(num, start, v=v)
            packets.append(packet_value)

    return start, v, expression_value(packets, id)


b = get_bin(num)
start = 0
start, versions, packet = decode(b, start)

print(f'Advent of Code Day 16 Answer Part 1: {sum(versions)}')

# Part 2

print(f'Advent of Code Day 16 Answer Part 2: {packet}')

