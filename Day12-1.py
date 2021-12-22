import numpy as np
from collections import defaultdict

filename = 'input_day12.txt'
input = np.loadtxt(filename, dtype=str)
#input = ['start-A','start-b','A-c','A-b','b-d','A-end','b-end']
size = len(input)

def create_dict(input):
    cave_map = defaultdict(list)
    for d in input:
        for line in d.splitlines():
            a, b = line.split("-")
            if a == 'start' or b == 'end':
                cave_map[a].append(b)
            else:
                cave_map[a].append(b)
                cave_map[b].append(a)
    return cave_map

cave_map = create_dict(input)

paths = []
def add_path(cave_map, position, path):
    path.append(position)
    for node in cave_map[position]:
        if node.isupper() or (node.islower() and node not in path):
            add_path(cave_map, node, path.copy())
    paths.append(path)

add_path(cave_map, 'start', [])

correct_paths = []
for path in paths:
    if path[-1] == 'end':
        correct_paths.append(path)

print(len(correct_paths))