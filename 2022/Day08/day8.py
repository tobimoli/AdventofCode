# %%
import os
import re

import numpy as np

# os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day07/')
with open("input_day8.txt", "r") as f:
    DATA = f.read().split("\n")

for i, line in enumerate(DATA):
    DATA[i] = [int(j) for j in list(line)]

DATA = np.array(DATA)


def is_on_edge(row, column, data):
    max_row, max_col = data.shape
    if row == 0:
        return True
    elif column == 0:
        return True
    elif row == max_row - 1:
        return True
    elif column == max_col - 1:
        return True
    else:
        return False


def is_visible(row, column, data):
    height = data[row, column]
    if is_on_edge(row, column, data):
        return True
    elif all(data[:row, column] < height):  # up
        return True
    elif all(data[row + 1 :, column] < height):  # down
        return True
    elif all(data[row, :column] < height):  # left
        return True
    elif all(data[row, column + 1 :] < height):  # right
        return True
    else:
        return False


def count_trues_until_false(lst: list):
    som = 0
    for item in lst:
        if item:
            som += 1
        else:
            som += 1
            return som
    return som


def count_visible_trees(data):
    nr_visible_trees = 0
    rows, columns = data.shape
    for row in range(rows):
        for col in range(columns):
            nr_visible_trees += is_visible(row, col, data)
    return nr_visible_trees


def see_nr_trees(row, column, data):
    height = data[row, column]
    factor = 1
    if is_on_edge(row, column, data):
        return 0
    else:
        # up
        factor *= count_trues_until_false(data[:row, column][::-1] < height)
        # down
        factor *= count_trues_until_false(data[row + 1 :, column] < height)
        # left
        factor *= count_trues_until_false(data[row, :column][::-1] < height)
        # right
        factor *= count_trues_until_false(data[row, column + 1 :] < height)
        return factor


def find_tree_house(data):
    max_score = 0
    rows, columns = data.shape
    for row in range(rows):
        for col in range(columns):
            factor = see_nr_trees(row, col, data)
            if factor > max_score:
                max_score = factor
    return max_score


# part 1
print(count_visible_trees(DATA))
# part 1
print(find_tree_house(DATA))

# %%
