# %%
import os
import re

import numpy as np

# os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day04/')
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


def add_files_to_dict(line: str, dir: list, dic: dict):
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
    directories = ["/"]
    for line in DATA:
        if line[:3] == "dir":
            directories.append(line[4:])
        if line[:4] == "$ cd":
            # change directory
            dir = change_directory(line, dir)
            dic = add_directory_to_dict(line, dir, dic)
        elif line[:4] == "$ ls":
            pass
        else:
            dic = add_files_to_dict(line, dir, dic)
    return dic, directories


def find_by_key1(dic: dict, dir: str):
    for key, value in dic.items():
        if key == dir:
            print(value)
        elif isinstance(value, dict):
            find_by_key1(value, dir)


def find_by_key(data, target):
    for k, v in data.items():
        if k == target:
            return v
        elif isinstance(v, dict):
            return find_by_key(v, target)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    return find_by_key(i, target)


def sum_directory(dic: dict, dir: str) -> int:
    som = 0

    return som


def sum_directories_at_most(n: int, dirs: list, dic: dict) -> int:
    som = 0
    for dir in dirs:
        s = sum_directory(dic, dir)
        if s <= n:
            som += s
    return som


dictionary, folders = make_dictionary({}, [])

# %%
