# %%
import os
import re

import numpy as np

# os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day04/')
with open("input_day6.txt", "r") as f:
    data = f.read().split("\n")


def find_first_n_unique_ch(string, n):
    length = len(string)
    substring = string[:n]
    i = 0
    while len(set(substring)) < n:
        i += 1
        substring = string[i : i + n]
    return i + n


string = data[0]
# part 1
print(find_first_n_unique_ch(string, 4))
# part 2
print(find_first_n_unique_ch(string, 14))
