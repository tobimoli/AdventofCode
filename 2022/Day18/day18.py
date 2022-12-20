# %%

import itertools
import json
import math
import os
import re

import numpy as np

DAY = str(18)

os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")

def read_data(data, outer=False):
    lst = []
    for line in data:
        x, y, z = line.split(',')
        lst.append([int(x), int(y), int(z)])
    if outer:
        lst += find_cubes_air(data)
    return lst

def make_empty_grid(data):
    x_max = y_max = z_max = 0
    for line in data:
        x, y, z = line.split(',')
        x_max = max(x_max, int(x))
        y_max = max(y_max, int(y))
        z_max = max(z_max, int(z))
    grid = np.zeros((x_max + 1, y_max + 1, z_max + 1))
    return grid

def fill_grid(data):
    grid = make_empty_grid(data)
    for line in data:
        x, y, z = line.split(',')
        grid[int(x), int(y), int(z)] = 1
    return grid

def neighbours(coordinate, grid):
    x, y, z = coordinate
    shape = grid.shape
    lst = []
    points = []
    if x > 0:
        points.append((x - 1, y, z))
    if y > 0:
        points.append((x, y - 1, z))
    if z > 0:
        points.append((x, y, z - 1))
    if x < shape[0] - 1:
        points.append((x + 1, y, z))
    if y < shape[1] - 1:
        points.append((x, y + 1, z))
    if z < shape[2] - 1:
        points.append((x, y, z + 1))
    for point in points:
        if grid[point] == 0:
            lst.append(point)
    return lst

def compute_distance(p1, p2):
    dist = 0
    for i in range(len(p1)):
        dist += abs(p1[i] - p2[i])
    return dist

def count_surface_area(data, outer=False):
    data_points = read_data(data, outer)
    surface_area = 6 * len(data_points)
    for i in range(len(data_points)):
        point1 = data_points[i]
        for j in range(i + 1, len(data_points)):
            point2 = data_points[j]
            if compute_distance(point1, point2) == 1:
                surface_area -= 2
    return surface_area

def is_edge(grid, cube):
    x, y, z = cube
    sh = grid.shape
    if x == 0 or y == 0 or z == 0:
        return True
    elif x == sh[0] - 1 or y == sh[1] - 1 or z == sh[2] - 1:
        return True
    else:
        return False

def is_cube_air(grid, cube, d):
    x, y, z = cube
    if grid[x, y, z] == 1:
        return False
    if is_edge(grid, cube):
        return False
    if find_edge(grid, d, cube, []):
        return False
    else:
        return True

def find_edge(grid, d, k, lst):
    # print(k)
    if is_edge(grid, k):
        return True
    else:
        lst.append(k)
        for v in d[k]:
            if v not in lst:
                edge = find_edge(grid, d, v, lst)
                if edge:
                    return True
    return False

def find_edge2(grid, dic, key, lst):
    print(key)
    lst.append(key)
    for item in dic[key]:
        if is_edge(grid, item):
            return True
    for item in dic[key]:
        if item not in lst:
            return find_edge2(grid, dic, item, lst)
    return False

def make_connections(data, grid):
    connections = {}
    sh = grid.shape
    for x in range(sh[0]):
        for y in range(sh[1]):
            for z in range(sh[2]):
                if grid[x, y, z] == 0:
                    if not is_edge(grid, [x, y, z]):
                        connections[(x, y, z)] = neighbours([x, y, z], grid)
    return connections

def find_cubes_air(data):
    grid = fill_grid(data)
    d = make_connections(data, grid)
    cubes_air = []
    sh = grid.shape
    for x in range(sh[0]):
        for y in range(sh[1]):
            for z in range(sh[2]):
                if is_cube_air(grid, (x, y, z), d):
                    # print([x, y, z])
                    cubes_air.append([x, y, z])
    return cubes_air

# part 1
print(count_surface_area(TEST))
print(count_surface_area(DATA))

# part 2
print(count_surface_area(TEST, outer=True))
print(count_surface_area(DATA, outer=True))


