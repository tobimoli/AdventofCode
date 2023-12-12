import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n")
f.close()

som_arrangements = 0

for row in data:
    arrangements = 1
    springs, info = row.split()

    # info
    info = [int(i) for i in info.split(",")]

    # springs
    springs = [i for i in springs.split(".") if i != ""]

    if len(springs) == len(info):
        for i, spring in enumerate(springs):
            nr = info[i]
            string = "#" * nr
