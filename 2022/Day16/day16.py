# %%

import itertools
import json
import math
import os
import re

import numpy as np

DAY = str(16)

# os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")


def get_info_from_line(line, dic):
    l = line.replace(",", "").replace("rate=", "").replace(";", "").split()
    dic[l[1]] = (int(l[4]), {o: 1 for o in l[9:]})
    return dic


def add_distances(dic):
    for k, i, j in itertools.product(dic, dic, dic):
        if i != j and j != k and k != i and k in dic[i][1] and j in dic[k][1]:
            t = dic[i][1][k] + dic[k][1][j]
            if dic[i][1].get(j, math.inf) > t:
                dic[i][1][j] = t
    return dic


def read(data):
    dic = {}
    for line in data:
        dic = get_info_from_line(line, dic)

    # add distances to each node for each node
    dic = add_distances(dic)
    # gebruik alleen de nodes die positieve flow_rate hebben
    dic = {
        kj: (vj[0], {ki: vi for ki, vi in vj[1].items() if dic[ki][0]})
        for kj, vj in dic.items()
        if vj[0] or kj == "AA"
    }

    return dic


def depth_first_search(p, o, t, node, w):
    global b
    if p > b:
        print(p)
    b = max(b, p)
    for sub_node, dist in dic[node][1].items():
        if sub_node not in o and t + dist + 1 < n:
            depth_first_search(
                p + (n - t - dist - 1) * dic[sub_node][0],
                o | set([sub_node]),
                t + dist + 1,
                sub_node,
                w,
            )
    if w == 0 and n == 26:
        depth_first_search(p, o, 0, "AA", 1)


#%% part 1
dic = read(DATA)
b = 0
n = 30
depth_first_search(0, set(), 0, "AA", 0)
print(b)

#%% part 2
b = 0
n = 26
depth_first_search(0, set(), 0, "AA", 0)
print(b)

# %%

# 2588 +
# 2790
