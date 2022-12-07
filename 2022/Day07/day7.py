# %%
import os
import re

import numpy as np

os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day07/')
with open("input_day7.txt", "r") as f:
    DATA = f.read().split("\n")


def change_directory(line: str, current_directory: list) -> list:
    if ".." in line:
        new_directory = current_directory[:-1]
    else:
        new_directory = current_directory + [line[5:]]
    return new_directory


def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic


def add_directory_to_dict(line: str, dir: list, dic: dict):
    if ".." not in line:
        d = dic
        for folder in dir[:-1]:
            d = d[folder]
        d[dir[-1]] = {}
    return dic


def add_files_to_dict(line: str, dir: list, dic: dict) -> dict:
    size, name = line.split(" ")
    d = dic
    for folder in dir:
        d = d[folder]
    if size == "dir":
        d[name] = {}
    else:
        d[name] = int(size)
    return dic


def make_dictionary(dic: dict, dir: list) -> dict:
    paths = []
    for line in DATA:
        if line[:4] == "$ cd":
            # change directory
            dir = change_directory(line, dir)
            dic = add_directory_to_dict(line, dir, dic)
            if dir not in paths:
                paths.append(dir)
        elif line[:4] == "$ ls":
            pass
        else:
            dic = add_files_to_dict(line, dir, dic)
    return dic, paths


def sum_directory(dic: dict) -> int:
    som = 0
    for _, value in dic.items():
        if not isinstance(value, dict):
            som += value
        else:
            som += sum_directory(value)
    return som


def make_list_of_sizes(dic, paths):
    lst = []
    for path_to_dir in paths:
        items = nested_get(dic, path_to_dir)
        s = sum_directory(items)
        lst.append(s)
    return lst


dictionary, paths = make_dictionary({}, [])
lst = make_list_of_sizes(dictionary, paths)

# part 1
print(sum([i for i in lst if i <= 100000]))

# part 2
total_disk_space = 70_000_000
update_space = 30_000_000
needed_space = update_space - (total_disk_space - lst[0])

print(min([i for i in lst if i >= needed_space]))