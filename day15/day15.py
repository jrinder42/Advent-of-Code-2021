
"""

Advent of Code 2021 - Day 15

"""

# thought we could only go down or to the right, which works for part 1

from copy import deepcopy
import heapq
import numpy as np

nums = []
with open('day15.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        nums.append([int(num) for num in line])

# Part 1

def create_graph(x):
    n = len(x)
    graph = {}
    for i in range(n):
        for j in range(n):
            vertex = i * n + j
            graph[vertex] = {}
            for pair in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ii, jj = i + pair[0], j + pair[1]
                if 0 <= ii < n and 0 <= jj < n:
                    new_vertex = ii * n + jj
                    graph[vertex].update({new_vertex: x[ii][jj]})
    return graph

# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Using_a_priority_queue
def dijkstra(graph, base, source, target=None):
    dist = {source: 0}  # could be {source: nums[source][source]}
    prev = {}

    hq = []
    heapq.heappush(hq, (dist[source], source))

    while hq:
        weight, u = heapq.heappop(hq)  # get the best vertex
        if target and u == target:
            s = []
            if prev.get(u, 0) or u == source:
                while u != source:
                    row, col = divmod(u, len(base))
                    s.append((u, base[row][col]))
                    u = prev[u]

            total = sum(dict(s).values())
            return total, s

        for v in graph[u]:
            alt = weight + graph[u][v]
            if v not in dist or alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(hq, (alt, v))

    return dist, prev

graph = create_graph(nums)
target = len(graph) - 1
d, p = dijkstra(graph=graph, base=nums, source=0, target=target)

print(f'Advent of Code Day 15 Answer Part 1: {d}')

# Part 2

v = []
for i in range(5):
    h = []
    for j in range(5):
        new_x = deepcopy(nums)
        for r in range(len(nums)):
            for c in range(len(nums[0])):
                val = nums[r][c] + i + j
                if val > 9:
                    new_x[r][c] = val - 9
                else:
                    new_x[r][c] = nums[r][c] + i + j

        if j == 0:
            h = new_x
        else:
            h = np.concatenate((h, new_x), axis=0)

    if i == 0:
        v = h
    else:
        v = np.concatenate((v, h), axis=1)

new_x = []
for row in range(v.shape[0]):
    new_x.append(v[row, :].tolist())

graph = create_graph(new_x)
target = len(graph) - 1
d, p = dijkstra(graph=graph, base=new_x, source=0, target=target)

print(f'Advent of Code Day 15 Answer Part 2: {d}')
