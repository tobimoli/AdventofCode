# %%
import os
import re

import numpy as np

# os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day04/')
with open("input_day7.txt", "r") as f:
    data = f.read().split("\n")

dictionary = {'/': {}}
current_directory = list(dictionary)

def change_directory(line: str, current_directory: list, d: dict) -> list:
    if '..' in line:
        new_directory = current_directory[:-1]
    else:
        new_directory = current_directory + [line[5:]]
    return new_directory

def make_dictionary(dic: dict, dir: list) -> dict:
    for line in data:
        if line[:4] == '$ cd':
            # change directory
            dir = change_directory(line, dir, dic)
        elif line[:4] == '$ ls':
            pass
        else:
            
    return dic


# %%
