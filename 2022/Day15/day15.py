# %%
import json
import os
import string
import re

import numpy as np

DAY = str(15)

os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")


def read(data):
    dic = {}
    for line in data:
        x_s, y_s, x_b, y_b = re.match("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()
        x_s, y_s, x_b, y_b = int(x_s), int(y_s), int(x_b), int(y_b)
        dic[(y_s, x_s)] = (y_b, x_b)
    return dic    

def distance_mh(pos1, pos2):
    return sum(abs(np.array(pos1) - np.array(pos2)))

def compute_answer(dic, row_nr):
    n = 1000000
    x_values = [i[1] for i in dic.keys()] + [i[1] for i in dic.values()]
    x_min = min(x_values)
    x_max = max(x_values)
    idx = list(range(x_min - n, x_max + 1 + n))
    print(idx[0], idx[-1])
    row = ['.'] * len(idx)
    for sensor, beacon in dic.items():
        print(sensor, beacon)
        dist = distance_mh(sensor, beacon)
        dist_row = distance_mh(sensor, (row_nr, sensor[1]))
        # als sensor is dichtbij genoeg, voeg # toe rondom dit (row_nr, sensor[1])
        min_afstand = dist - dist_row
        if min_afstand >= 0:
            row[idx.index(sensor[1] - min_afstand) : idx.index(sensor[1] + min_afstand + 1)] = ['#'] * (min_afstand * 2 + 1)

    for sensor, beacon in dic.items():
        if sensor[0] == row_nr:
            row[idx.index(sensor[1])] = 'S'
        if beacon[0] == row_nr:
            row[idx.index(beacon[1])] = 'B'
    return row


def do_one_row(dic, size, row_nr) -> list:
    idx = list(range(size + 1))
    row = ['.'] * len(idx)
    # print(idx)
    for sensor, beacon in dic.items():
        dist = distance_mh(sensor, beacon)
        dist_row = distance_mh(sensor, (row_nr, sensor[1]))
        # als sensor is dichtbij genoeg, voeg # toe rondom dit (row_nr, sensor[1])
        min_afstand = dist - dist_row
        if min_afstand >= 0:
            l = max(sensor[1] - min_afstand, 0)
            r = min(sensor[1] + min_afstand + 1, size)
            print(idx.index(l), idx.index(r), len(row))
            row[idx.index(l) : idx.index(r)] = ['#'] * (r - l + 1)

    for sensor, beacon in dic.items():
        if sensor[1] <= size:
            if sensor[0] == row_nr:
                row[idx.index(sensor[1])] = 'S'
            if beacon[0] == row_nr:
                row[idx.index(beacon[1])] = 'B'
    return row


def main(data, row_nr):
    dic = read(data)
    answer = compute_answer(dic, row_nr)
    return answer.count('#')


def main2(data, size):
    dic = read(data)
    print(list(range(size+1)))
    for row_nr in range(size + 1):
        print(f"row_nr: {row_nr}")
        row = do_one_row(dic, size, row_nr)
        print(row)
        print(row.count('.'))
        if row.count('.') == 1:
            x = row.index('.')
            break
    print(row_nr, x)
    return 4000000 * row_nr + x


# part 1
# print(main(TEST, 10))
# print(main(DATA, 2000000))

# part 2
print(main2(TEST, 20))
# print(main2(DATA))

# %%
