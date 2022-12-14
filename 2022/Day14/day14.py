# %%
import json
import os
import string

import numpy as np

DAY = str(14)

# os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")


def read(data, part2=False):
    n = 500
    s = 200
    cave = []
    minx, maxx, maxy = n, n, 0

    for line in data:
        coordinates = line.split(" -> ")
        for coordinate in coordinates:
            x, y = coordinate.split(",")
            x, y = int(x), int(y)
            if x < minx:
                minx = x
            elif x > maxx:
                maxx = x
            if y > maxy:
                maxy = y
    cave = np.zeros(shape=(maxy + 3, maxx + s))
    for line in data:
        coordinates = line.split(" -> ")
        for i, coordinate in enumerate(coordinates[:-1]):
            x1, y1 = coordinate.split(",")
            x2, y2 = coordinates[i + 1].split(",")
            x1, y1 = int(x1), int(y1)
            x2, y2 = int(x2), int(y2)
            if x1 == x2:  # verticale muur
                if y1 <= y2:
                    cave[y1 : y2 + 1, x1] = 1
                else:
                    cave[y2 : y1 + 1, x1] = 1
            else:
                if x1 <= x2:
                    cave[y1, x1 : x2 + 1] = 1
                else:
                    cave[y1, x2 : x1 + 1] = 1
    if part2:
        cave[maxy + 2, :] = 1
    cave[0, n] = 8
    return cave[:, minx - s :]


def simulate_one_sand(grid):
    y_source = 0
    x_source = np.where(grid[y_source] == 8)[0][0]
    x_in = x_source
    y_in = y_source
    condition = True
    rest = False
    while condition:
        if y_in == grid.shape[0] - 1:
            rest = False
            condition = False
        elif x_in == 0:
            rest = False
            condition = False
        elif x_in == grid.shape[1] - 1:
            rest = False
            condition = False
        elif grid[y_in + 1, x_in] == 0:
            grid[y_in, x_in] = 0
            y_in = y_in + 1
            grid[y_in, x_in] = -1
        elif grid[y_in + 1, x_in - 1] == 0:
            grid[y_in, x_in] = 0
            y_in = y_in + 1
            x_in = x_in - 1
            grid[y_in, x_in] = -1
        elif grid[y_in + 1, x_in + 1] == 0:
            grid[y_in, x_in] = 0
            y_in = y_in + 1
            x_in = x_in + 1
            grid[y_in, x_in] = -1
        else:
            condition = False
            rest = True
    grid[y_source, x_source] = 8
    return grid, rest, rest


def simulate_one_sand2(grid):
    y_source = 0
    x_source = np.where(grid[y_source] == 8)[0][0]
    x_in = x_source
    y_in = y_source
    condition = True
    rest = False
    while condition:
        if grid[y_in + 1, x_in] == 0:
            grid[y_in, x_in] = 0
            y_in = y_in + 1
            grid[y_in, x_in] = -1
        elif grid[y_in + 1, x_in - 1] == 0:
            grid[y_in, x_in] = 0
            y_in = y_in + 1
            x_in = x_in - 1
            grid[y_in, x_in] = -1
        elif grid[y_in + 1, x_in + 1] == 0:
            grid[y_in, x_in] = 0
            y_in = y_in + 1
            x_in = x_in + 1
            grid[y_in, x_in] = -1
        else:
            condition = False
            rest = True
    stop = True
    if y_in == 0:
        stop = False
    grid[y_source, x_source] = 8
    return grid, rest, stop


def simulate_sand(grid, func=simulate_one_sand):
    condition = True
    amount = 0
    while condition:
        grid, rest, condition = func(grid)
        if rest:
            amount += 1
    return amount


def main(data):
    grid = read(data)
    answer = simulate_sand(grid)
    return answer


def main2(data):
    grid = read(data, True)
    answer = simulate_sand(grid, simulate_one_sand2)
    print(grid)
    return answer


# part 1
print(main(TEST))
print(main(DATA))

# part 2
print(main2(TEST))
print(main2(DATA))

# %%
