# %%

import itertools
import json
import math
import os
import re

import numpy as np

DAY = str(17)

os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")

ROCKS = [[(0, 2), (0, 3), (0, 4), (0, 5)],
        [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)],
        [(0, 4), (1, 4), (2, 2), (2, 3), (2, 4)],
        [(0, 2), (1, 2), (2, 2), (3, 2)],
        [(0, 2), (0, 3), (1, 2), (1, 3)]]
GRID_START = np.zeros((1, 7))


def get_number_empty_rows(grid):
    n_rows = 0
    for row in grid:
        if np.sum(row) == 0:
            n_rows += 1
        else:
            break
    return n_rows

def move_rock(grid, delta_row, delta_col):
    rock_rows, rock_cols = np.where(grid == 2)
    old_items = []
    new_items = []
    for rock_row, rock_col in zip(rock_rows, rock_cols):
        old_items.append((rock_row, rock_col))
        new_items.append((rock_row + delta_row, rock_col + delta_col))
    
    for items in new_items:
        if grid[items] == 1:
            return grid

    for items in old_items:
        grid[items] = 0
    for items in new_items:
        grid[items] = 2
    return grid

def new_rock(grid, rock):
    # print("Rock starts falling")
    # compute number of extra rows needed
    n_empty_rows = get_number_empty_rows(grid)
    rows_rock = 1
    for rock_item in rock:
        rows_rock = max(rows_rock, rock_item[0] + 1)
    extra_rows = 3 - n_empty_rows + rows_rock
    # add empty rows on top
    if extra_rows > 0:
        grid = np.insert(grid, 0, [[0] * 7] * extra_rows, axis=0)
    elif extra_rows < 0:
        grid = grid[abs(extra_rows):]
    # add rock
    for rock_item in rock:
        grid[rock_item[0], rock_item[1]] = 2
    return grid

def rock_push(grid, push):
    # print("Rock got pushed to " + push)
    _, rock_cols = np.where(grid == 2)
    if push == '<':
        if 0 not in rock_cols:
            grid = move_rock(grid, 0, -1)
    else:
        if 6 not in rock_cols:
            grid = move_rock(grid, 0, +1)
    return grid

def hit_bottom(grid) -> bool:
    n_rows, _ = grid.shape
    rock_rows, rock_cols = np.where(grid == 2)
    for rock_row, rock_col in zip(rock_rows, rock_cols):
        if rock_row + 1 == n_rows:
            # print("Rock falls to rest")
            return True
        if grid[rock_row + 1, rock_col] == 1:
            # print("Rock falls to rest")
            return True
    return False

def rock_fall(grid):
    # print("Rock falls 1 unit")
    grid = move_rock(grid, +1, 0)
    return grid

def find_pattern(lst: list):
    length = len(lst)
    for i in range(3, length // 3):
        pattern = lst[:i]
        next_pattern = lst[i: 2 * i]
        if pattern == next_pattern:
            return pattern
    return False

def compute_pattern(data):
    grid = GRID_START
    cycle_len = len(data)
    cycle_rock = len(ROCKS)
    # n_rocks = cycle_len * cycle_rock
    old_size = 0
    push_nr = 0
    rock_nr = 0
    heights_used = []
    for i in range(60):
        if i == 0:
            n_rocks = 1719
        else:
            n_rocks = 1725
        new_size, grid, push_nr, rock_nr = main(grid, data, n_rocks, size=old_size, push_nr=push_nr, rock_nr=rock_nr)
        heights_used.append(new_size - old_size)
        print(n_rocks, new_size, new_size - old_size, rock_nr)
        old_size = new_size
    pattern = find_pattern(heights_used[2:])
    return n_rocks, sum(heights_used[:2]), pattern

def main(grid, data, n_rocks, size=0, push_nr=0, rock_nr=0):
    n_empty_rows = get_number_empty_rows(grid)
    length = len(grid)
    size_so_far = length - n_empty_rows
    size -= size_so_far
    for i in range(n_rocks):
        rock = ROCKS[(i + rock_nr) % len(ROCKS)]
        # new rock
        grid = new_rock(grid, rock)
        
        # first push
        push = data[push_nr % len(data)]
        grid = rock_push(grid, push)
        push_nr += 1

        rock_hits_bottom = hit_bottom(grid)
        while not rock_hits_bottom:
            # rock falling 1 unit
            grid = rock_fall(grid)
            
            # push rock
            push = data[push_nr % len(data)]
            grid = rock_push(grid, push)
            push_nr += 1
            if hit_bottom(grid):
                rock_hits_bottom = True
                rock_rows, rock_cols = np.where(grid == 2)
                for rock_row, rock_col in zip(rock_rows, rock_cols):
                    grid[rock_row, rock_col] = 1
        # print(push_nr % len(data), i, (i + rock_nr + 1) % len(ROCKS))
        if push_nr % len(data) == 0:
            print(push_nr, i + 1, (i + rock_nr + 1) % len(ROCKS))
        length = len(grid)
        grid = grid[:50]
        size += max(0, length - 50)
    n_empty_rows = get_number_empty_rows(grid)
    length = len(grid)
    return length - n_empty_rows + size, grid, push_nr, (i + rock_nr + 1) % len(ROCKS)


# part 1
size, _, _, _ = main(GRID_START, TEST[0], 2022)
print(size)
size, _, _, _ = main(GRID_START, DATA[0], 2022)
print(size)

# part 2
d = DATA[0]
N_ROCKS = 1_000_000_000_000

sample, size, pattern = compute_pattern(d)

if pattern == False:
    print("No pattern found")

length = len(pattern)
full_cycles = (N_ROCKS - sample) // (length * sample)
rest_cycle = ((N_ROCKS - sample) % (length * sample))
size += full_cycles * sum(pattern)

print(size)

if rest_cycle > 0:
    # first do one cycle to get the grid and push_nr
    _, grid, push_nr, rock_nr = main(GRID_START, d, sample * (len(pattern) + 2))
    size, _, _, _ = main(grid, d, rest_cycle, size=size, push_nr=push_nr, rock_nr=rock_nr)

print(size)
# %%
# start = 31749
# 1569900312888
# 1514285714288
# 1569900571649 too low
# 1569910571649 too low
# 1570930232582
# %%
from itertools import cycle
from collections import defaultdict

inp = cycle(enumerate(open(f"input_day{DAY}.txt").read()))
rocks = cycle(  # rows of bits
    enumerate([[120], [32, 112, 32], [112, 16, 16], [64, 64, 64, 64], [96, 96]])
)
M = []  # map
S = []  # sequence of positions of rocks at rest
R = defaultdict(list)  # (rock_idx, instruction_idx) -> S_idx
H = []  # sequence of max heights
L = C = Z = 0  # prefix, cycle length and height per cycle


def fits(rk, x, y):
    return not any(
        M[j] & rk[j - y] >> x for j in range(y, min(len(M), y + len(rk)))
    ) and all(r >> x << x == r for r in rk)


while not C:
    ri, rock = next(rocks)
    x, y = 2, len(M) + 4
    # play rock
    while y and fits(rock, x, y - 1):
        y -= 1
        ai, arrow = next(inp)
        nx = max(0, x - 1) if arrow == "<" else min(7, x + 1)
        x = nx if fits(rock, nx, y) else x

    # update map
    for j, r in enumerate(rock, y):
        if j < len(M):
            M[j] |= r >> x
        else:
            M.append(r >> x)
    H.append(len(M))
    S.append(x)

    # find cycle
    R[(ri, ai)].append(len(S))
    for i, m in enumerate(R[(ri, ai)][:-1]):
        for b in R[(ri, ai)][:i]:
            if m - b == len(S) - m and S[b:m] == S[m:]:
                L, C, Z = m, m - b, len(M) - H[m-1]

height = lambda iters: (Z * ((iters - L) // C) + H[L+((iters - L) % C)-1])
print ("Part1: ", height(2022))
print ("Part2: ", height(1000000000000))

# %%
