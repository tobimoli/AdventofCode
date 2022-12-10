# %%
import os
import re

import numpy as np

os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day10/')
with open("input_day10.txt", "r") as f:
    DATA = f.read().split("\n")

def check_cycle(cycle, number):
    if (cycle - 20) % 40 == 0:
        print(number, cycle)
        return number * cycle
    else:
        return 0

def make_sprite(number):
    numbers = [number - 1, number, number + 1]
    sprite = [0] * 40
    for n in numbers:
        if n >= 0 and n<=39:
            sprite[n] = 1
    return sprite 

def add_pixel(sprite, cycle):
    if sprite[cycle % 40] == 1:
        return '#'
    else:
        return '.'

number = 1
sprite = make_sprite(number)
cycle_during = 1
answer = 0
string = ''
for line in DATA:

    string += add_pixel(sprite, cycle_during - 1)
    cycle_during += 1
    answer += check_cycle(cycle_during, number)
    if line != 'noop':

        _, value = line.split(' ')
        number += int(value)
        string += add_pixel(sprite, cycle_during - 1)
        
        sprite = make_sprite(number)
        cycle_during += 1
        answer += check_cycle(cycle_during, number)

# part 1
print(answer)

# part 2
for i in range(6):
    print(string[i*40: (i+1)*40])