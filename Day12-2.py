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
            elif a == 'end' or b == 'start':
                cave_map[b].append(a)
            else:
                cave_map[a].append(b)
                cave_map[b].append(a)
    return cave_map
def small_letter_check(path):
    total = 0
    SET = set(path[1:-1])
    for node in SET:
        if node.islower() and path.count(node) == 2:
            total += 1
    if total <= 1:
        return True
    else:
        return False
def small_letter_check2(path, node):
    total = 0
    SET = set(path[1:])
    SET.add(node)
    for node in SET:
        if node.islower() and path.count(node) == 2:
            total += 1
    if total <= 1:
        return True
    else:
        return False  

cave_map = create_dict(input)

paths = 0
def add_path(cave_map, position, path):
    path.append(position)
    for node in cave_map[position]:
        if node.isupper() or (node.islower() and path.count(node)<2):
            add_path(cave_map, node, path.copy())
    if path[-1] == 'end':
        if small_letter_check(path):
            print(path)
            global paths
            paths += 1
    
add_path(cave_map, 'start', [])

print(paths)
#137948

def add_path2(cave_map, node, visited):
    paths = []
    new_visit = visited + [node]
    if node == 'end':
        return [new_visit]
    for n in cave_map[node]:
        if n != 'start':
            if n.isupper():
                temp_res = add_path2(cave_map, n, new_visit)
                paths.extend(temp_res)
            else:
                lower = [i for i in new_visit if i.islower()]
                twice = any([True for i in lower if lower.count(i) > 1])
                if (twice and new_visit.count(n) < 1) or (not twice and new_visit.count(n) < 2):
                    temp_res = add_path2(cave_map, n, new_visit)
                    paths.extend(temp_res)
    return paths

print(len(add_path2(cave_map,'start',[])))