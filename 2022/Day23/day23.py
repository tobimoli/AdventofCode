# %%
import re

import numpy as np

DAY = str(23)

# os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")


def print_locs(locs):
    r_min = c_min = 0
    for loc in locs:
        r, c = loc
        r_min = min(r_min, r)
        c_min = min(c_min, c)

    grid = np.zeros((6, 6))
    for loc in locs:
        r, c = loc
        grid[(r - r_min, c - c_min)] = 1
    return grid


def read_data(data):
    location_elves = []
    for i, line in enumerate(data):
        for j, item in enumerate(line):
            if item == "#":
                location_elves.append((i, j))
    return location_elves


def compute_answer(locs):
    row_min, row_max = None, None
    col_min, col_max = None, None
    for loc in locs:
        row, col = loc
        row_min = row if row_min is None else min(row_min, row)
        row_max = row if row_max is None else max(row_max, row)
        col_min = row if col_min is None else min(col_min, col)
        col_max = row if col_max is None else max(col_max, col)
    rows = row_max - row_min + 1
    cols = col_max - col_min + 1
    cells = rows * cols
    empty_cells = cells - len(locs)
    return empty_cells


def check_surrounding(loc, locs, nr):
    row, col = loc
    n_locs = [(row - 1, col + i) for i in [-1, 0, 1]]
    s_locs = [(row + 1, col + i) for i in [-1, 0, 1]]
    e_locs = [(row + i, col + 1) for i in [-1, 0, 1]]
    w_locs = [(row + i, col - 1) for i in [-1, 0, 1]]

    all_locs = n_locs + s_locs + e_locs + w_locs
    check_all = [loc in locs for loc in all_locs]
    if sum(check_all) == 0:
        return loc
    else:
        dic = {0: n_locs, 1: s_locs, 2: w_locs, 3: e_locs}
        for i in range(nr, nr + 4):
            i_locs = dic[i % 4]
            check = [loc in locs for loc in i_locs]
            if sum(check) == 0:
                return i_locs[1]
    return loc


def do_one_round(locs, nr):
    # eerst helft, kijk waar elven heen willen
    proposed_locs = []
    for loc in locs:
        proposed_locs.append(check_surrounding(loc, locs, nr))
    # tweede helft
    final_locs = []
    for idx, p_loc in enumerate(proposed_locs):
        if sum([p_loc == loc for loc in proposed_locs]) == 1:
            final_locs.append(p_loc)
        else:
            final_locs.append(locs[idx])
    return final_locs


def do_rounds(locs, n):
    for i in range(n):
        print(i)
        locs = do_one_round(locs, i)
    return locs


def main(data):
    location_elves = read_data(data)
    location_elves = do_rounds(location_elves, 10)
    answer = compute_answer(location_elves)
    return answer


# part 1
print(main(TEST))
print(main(DATA))


# %%
