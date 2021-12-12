
"""

Advent of Code 2021 - Day 12

"""

from collections import defaultdict

caves = defaultdict(list)
with open('day12.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip('\n')
        l, r = line.split('-')
        caves[l].append(r)
        caves[r].append(l)

# Part 1

# dijkstra's algorithm

# https://stackoverflow.com/questions/24471136/how-to-find-all-paths-between-two-graph-nodes
def find_all_paths(graph, start, end, path=None, p2=False):
    if path is None:
        path = []

    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if p2:
            condition = True
            # if node is in the current path
            if node in path and node.islower():
                value = ''
                for p in path:
                    if p == 'start':
                        continue
                    # if the same 2 small caves have already been explored
                    if p.islower() and path.count(p) > 1:
                        value = p
                        break

                # go to start + end before start again
                if node == 'start' or value:
                    condition = False
        else:
            condition = node.lower() not in path

        if condition:
            new_paths = find_all_paths(graph, node, end, path, p2=p2)
            for new_path in new_paths:
                paths.append(new_path)

    return paths

x = find_all_paths(caves, 'start', 'end')
print(f'Advent of Code Day 12 Answer Part 1: {len(x)}')

# Part 2

x = find_all_paths(caves, 'start', 'end', p2=True)
print(f'Advent of Code Day 12 Answer Part 2: {len(x)}')
