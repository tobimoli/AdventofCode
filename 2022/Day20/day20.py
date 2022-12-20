# %%

import itertools
import json
import math
import os
import re
import collections

import numpy as np

DAY = str(20)

os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")

def read_data(data, multiplier):
    lst = []
    for i in data:
        lst.append(int(i) * multiplier)
    return lst

def mix_lst(lst, rounds):
    length = len(lst)
    koppel_lijst = list(range(length))
    koppel_dict = dict(zip(koppel_lijst, lst))
    mix = koppel_lijst.copy()
    for _ in range(rounds):
        for i in koppel_lijst:
            idx_old = mix.index(i)
            number = koppel_dict[i]
            idx_new = idx_old + number

            del mix[idx_old]

            mix.insert((idx_new + length - 1) % (length - 1), i)

    mix = [koppel_dict[i] for i in mix]
    return mix

def find_answer(mix):
    length = len(mix)
    idx_0 = mix.index(0)
    return sum([mix[(idx_0 + (i+1)*1000) % length] for i in range(3)])

def main(data, rounds = 1, decription = 1):
    lst = read_data(data, decription)
    mix = mix_lst(lst, rounds)
    answer = find_answer(mix)
    return answer

# part 1
print(main(TEST))
print(main(DATA))

# part 2
DECRYPPTION_KEY = 811589153
print(main(TEST, 10, DECRYPPTION_KEY))
print(main(DATA, 10, DECRYPPTION_KEY))

# %%
# 15875 too high
# 4151
# 7848878698663
# %%
from collections import defaultdict

InputList = []
with open(f"input_day{DAY}.txt") as data:
    for t in data:
        Line = t.strip()
        Line = int(Line)
        InputList.append(Line)

#this confirms that the values are not unique
InputSet = set(InputList)
#print(len(InputList), len(InputSet))

Len = len(InputList)
InputDict = defaultdict()
for n, v in enumerate(InputList):
    InputDict[n] = v
    if v == 0:
        ZeroIndex = n

NeighborDict = defaultdict()
for v in range(Len):
    NewNeighbors = ((v-1)%Len, (v+1)%Len)
    NeighborDict[v] = NewNeighbors

for v in range(Len):
    #Discovering this minus 1 took some doing
    Movement = InputDict[v] % (Len-1)
    if Movement == 0:
        continue
    StartBackNeighbor, StartForwardNeighbor = NeighborDict[v]
    CurrentSpot = v
    NextSpot = StartForwardNeighbor
    
    for f in range(Movement):
        _, MidFN = NeighborDict[NextSpot]
        CurrentSpot = NextSpot
        NextSpot = MidFN
    EndSpot = CurrentSpot
    
    SBNB, _ = NeighborDict[StartBackNeighbor]
    NeighborDict[StartBackNeighbor] = (SBNB, StartForwardNeighbor)

    _, SFNF = NeighborDict[StartForwardNeighbor]
    NeighborDict[StartForwardNeighbor] = (StartBackNeighbor, SFNF)

    EndSpotBack, EndSpotForward = NeighborDict[EndSpot]
    NeighborDict[EndSpot] = (EndSpotBack, v)

    NeighborDict[v] = (EndSpot, EndSpotForward)

    _, ESFF = NeighborDict[EndSpotForward]
    NeighborDict[EndSpotForward] = (v, ESFF)

Part1Answer = 0
CurrentSpot = ZeroIndex
_, NextSpot = NeighborDict[CurrentSpot]
for t in range(3):
    for f in range(1000):
        _, MidFN = NeighborDict[NextSpot]
        CurrentSpot = NextSpot
        NextSpot = MidFN
    Part1Answer += InputDict[CurrentSpot]

########Part 2
DecryptionKey = 811589153
for v in range(Len):
    Rea = InputDict[v]
    InputDict[v] = Rea*DecryptionKey

for v in range(Len):
    NewNeighbors = ((v-1)%Len, (v+1)%Len)
    NeighborDict[v] = NewNeighbors

for t in range(10):
    print(t)
    for v in range(Len):
        Movement = InputDict[v] % (Len-1)
        if Movement == 0:
            continue
        StartBackNeighbor, StartForwardNeighbor = NeighborDict[v]
        CurrentSpot = v
        NextSpot = StartForwardNeighbor

        for f in range(Movement):
            _, MidFN = NeighborDict[NextSpot]
            CurrentSpot = NextSpot
            NextSpot = MidFN
        EndSpot = CurrentSpot

        SBNB, _ = NeighborDict[StartBackNeighbor]
        NeighborDict[StartBackNeighbor] = (SBNB, StartForwardNeighbor)

        _, SFNF = NeighborDict[StartForwardNeighbor]
        NeighborDict[StartForwardNeighbor] = (StartBackNeighbor, SFNF)

        EndSpotBack, EndSpotForward = NeighborDict[EndSpot]
        NeighborDict[EndSpot] = (EndSpotBack, v)

        NeighborDict[v] = (EndSpot, EndSpotForward)

        _, ESFF = NeighborDict[EndSpotForward]
        NeighborDict[EndSpotForward] = (v, ESFF)


Part2Answer = 0
CurrentSpot = ZeroIndex
_, NextSpot = NeighborDict[CurrentSpot]
for t in range(3):
    for f in range(1000):
        _, MidFN = NeighborDict[NextSpot]
        CurrentSpot = NextSpot
        NextSpot = MidFN
    Part2Answer += InputDict[CurrentSpot]
    print(InputDict[CurrentSpot])

      
# print(f"{Part1Answer = }")
# print(f"{Part2Answer = }")
# %%
