# %%
import os
import re
import numpy as np
os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2020/Day03/')

with open('input_day3.txt', 'r') as f:
    data = f.read().split('\n')

def bereken_aantal_bomen(right, down):
    position = [0, 0]
    aantal_bomen = 0
    while position[0] + down < DEPTH:
        position[0] += down
        position[1] += right

        position[1] = position[1] % LENGTH

        if data[position[0]][position[1]] == '#':
            aantal_bomen += 1
    return aantal_bomen

DEPTH = len(data)
LENGTH = len(data[0])

# part 1
print(bereken_aantal_bomen(3, 1))

# part 2
RIGHTS = [1, 3, 5, 7, 1]
DOWNS = [1, 1, 1, 1, 2]
aantal_bomen_lst = []
for right, down in zip(RIGHTS, DOWNS):
    aantal_bomen_lst.append(bereken_aantal_bomen(right, down))

product = 1
for aantal_bomen in aantal_bomen_lst:
    product *= aantal_bomen

print(product)