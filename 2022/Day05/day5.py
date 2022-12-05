# %%
import os
import re

import numpy as np

# os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day04/')
with open("input_day5.txt", "r") as f:
    data = f.read().split("\n")


def get_start_position(data):
    # make dictionary with numbers as keys and crates in list as value
    length = len(data[0])
    nr_of_columns = length // 4 + 1
    dic = {key: [] for key in range(1, nr_of_columns + 1)}
    for idx, line in enumerate(data):
        if line == "":
            size_columns = idx - 1
    for nr in range(1, nr_of_columns + 1):
        idx = 4 * nr - 3
        for line in data[:size_columns]:
            if line[idx] != " ":
                dic[nr].append(line[idx])
    return dic, size_columns + 2


def apply_movement(amount, nr_from, nr_to, dic, type):
    # pas de regel toe
    if type == 9000:
        for _ in range(amount):
            crate = dic[nr_from][0]
            dic[nr_to] = [crate] + dic[nr_to]
            dic[nr_from] = dic[nr_from][1:]
    elif type == 9001:
        crates = dic[nr_from][:amount]
        dic[nr_to] = crates + dic[nr_to]
        dic[nr_from] = dic[nr_from][amount:]
    return dic


def apply_movements(crates, lines, type):
    for movement in lines:
        amount, nr_from, nr_to = map(
            int, re.match("move (\d+) from (\d+) to (\d+)", movement).groups()
        )
        crates = apply_movement(amount, nr_from, nr_to, crates, type)
    return crates


def get_top_of_crates(crates):
    string = ""
    for _, value in crates.items():
        string += value[0]
    return string


# part 1
crates, size = get_start_position(data)
crates = apply_movements(crates, data[size:], 9000)
print(get_top_of_crates(crates))


# part 2
crates, size = get_start_position(data)
crates = apply_movements(crates, data[size:], 9001)
print(get_top_of_crates(crates))

# %%
