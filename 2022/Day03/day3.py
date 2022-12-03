# %%
import os

import numpy as np

with open("input_day3.txt", "r") as f:
    data = f.read().split("\n")

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet_lower.upper()

PRIO = dict(zip(alphabet_lower + alphabet_upper, list(range(1, 2 * len(alphabet_lower) + 1))))

# Part 1
priority = 0
for rucksack in data:
    number_of_items = len(rucksack)
    compartment1, compartment2 = rucksack[:number_of_items // 2], rucksack[number_of_items // 2:]
    common_items = list(set(compartment1)&set(compartment2))
    for common_item in common_items:
        priority += PRIO[common_item]

print(priority)

# Part 2
number_of_elves = len(data)
number_of_groups = number_of_elves // 3

priority = 0
for group_number in range(number_of_groups):
    rucksacks = data[group_number * 3 : (group_number + 1) * 3]
    common_items = list(set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2]))
    for common_item in common_items:
        priority += PRIO[common_item]

print(priority)
