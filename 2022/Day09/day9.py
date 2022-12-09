# %%
import os
import re

import numpy as np

# os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day07/')
with open("input_day9.txt", "r") as f:
    DATA = f.read().split("\n")


def change_pos_head(pos_head, direction):
    last_pos_head = pos_head[-1].copy()
    new_pos_head = last_pos_head
    if direction == "U":
        new_pos_head[0] += 1
    elif direction == "D":
        new_pos_head[0] -= 1
    elif direction == "R":
        new_pos_head[1] += 1
    elif direction == "L":
        new_pos_head[1] -= 1
    pos_head.append(new_pos_head)
    return pos_head


def change_pos_tail(pos_head, pos_tail):
    last_pos_head = pos_head[-1].copy()
    last_pos_tail = pos_tail[-1].copy()
    new_pos_tail = last_pos_tail

    rij_verschil = last_pos_tail[0] - last_pos_head[0]
    kolom_verschil = last_pos_tail[1] - last_pos_head[1]

    if abs(rij_verschil) == 0:  # zelfde rij
        if abs(kolom_verschil) == 2:  # verschillende kolom
            new_pos_tail[1] -= kolom_verschil // 2
    elif abs(rij_verschil) == 1:
        if abs(kolom_verschil) == 2:
            new_pos_tail[0] -= rij_verschil
            new_pos_tail[1] -= kolom_verschil // 2
    elif abs(rij_verschil) == 2:  # verschillende rij
        if abs(kolom_verschil) == 0:  # zelfde kolom
            new_pos_tail[0] -= rij_verschil // 2
        elif abs(kolom_verschil) == 1:  # verschillende kolom
            new_pos_tail[1] -= kolom_verschil
            new_pos_tail[0] -= rij_verschil // 2
    pos_tail.append(new_pos_tail)
    return pos_tail


def count_unique_positions(lst: list):
    """Count unique occurances in list."""
    lst_unique = []
    for item in lst:
        if item not in lst_unique:
            lst_unique.append(item)
    return len(lst_unique)


def main1():
    pos_tail = [[0, 0]]
    pos_head = [[0, 0]]
    for line in DATA:
        direction, size = line.split(" ")
        for _ in range(int(size)):
            pos_head = change_pos_head(pos_head, direction)
            pos_tail = change_pos_tail(pos_head, pos_tail)
    
    print(count_unique_positions(pos_tail))

# part 1
main1()

# part 2

def main2(n):
    positions = [[[0, 0]]] * (1 + n)
    for line in DATA:
        direction, size = line.split(" ")
        for _ in range(int(size)):
            print(positions[0])
            positions[0] = change_pos_head(positions[0], direction)
            for tail_nr in range(1, 1 + n):
                positions[tail_nr] = change_pos_tail(positions[tail_nr - 1], positions[tail_nr])
    
    print(count_unique_positions(positions[-1]))