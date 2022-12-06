# %%
import os
import re
import numpy as np
os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2020/Day07/')

with open('input_day7.txt', 'r') as f:
    data = f.read().split('\n')

# data to dictionary
dic = {}
for line in data:
    color, contains = line.split(' bags contain ')
    colors = contains.split(', ')
    dic[color] = {}
    if 'no other bags.' not in colors:
        for c in colors:
            important_bit = c.split(' bag')[0]
            nr_of_bags = important_bit[0]
            color_i = important_bit[2:]
            dic[color][color_i] = int(nr_of_bags)

def contains_your_bag(color):
    if color == "shiny gold": 
        return True
    else:
        return any(contains_your_bag(c) for c, _ in dic[color].items())

# part 1
nr_bags = 0
for bag in dic:
    if contains_your_bag(bag):
        nr_bags += 1
print(nr_bags - 1)

# part 2
def count_bags(bag_type):
    return 1 + sum(number * count_bags(color) for color, number in dic[bag_type].items())

print(count_bags("shiny gold") - 1)