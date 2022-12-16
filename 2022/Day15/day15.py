# %%

import json
import os
import re
import string
import time

import numpy as np

DAY = str(15)

# os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")


def read(data):
    dic = {}
    for line in data:
        x_s, y_s, x_b, y_b = re.match(
            "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
            line,
        ).groups()
        x_s, y_s, x_b, y_b = int(x_s), int(y_s), int(x_b), int(y_b)
        dic[(y_s, x_s)] = (y_b, x_b)
    return dic


def distance_mh(pos1, pos2):
    a, b = pos1
    c, d = pos2
    return abs(a - c) + abs(b - d)


def compute_answer(dic, row_nr):
    n = 1000000
    x_values = [i[1] for i in dic.keys()] + [i[1] for i in dic.values()]
    x_min = min(x_values)
    x_max = max(x_values)
    idx = list(range(x_min - n, x_max + 1 + n))
    print(idx[0], idx[-1])
    row = ["."] * len(idx)
    for sensor, beacon in dic.items():
        print(sensor, beacon)
        dist = distance_mh(sensor, beacon)
        dist_row = distance_mh(sensor, (row_nr, sensor[1]))
        # als sensor is dichtbij genoeg, voeg # toe rondom dit (row_nr, sensor[1])
        min_afstand = dist - dist_row
        if min_afstand >= 0:
            row[
                idx.index(sensor[1] - min_afstand) : idx.index(
                    sensor[1] + min_afstand + 1
                )
            ] = ["#"] * (min_afstand * 2 + 1)

    for sensor, beacon in dic.items():
        if sensor[0] == row_nr:
            row[idx.index(sensor[1])] = "S"
        if beacon[0] == row_nr:
            row[idx.index(beacon[1])] = "B"
    return row


def do_one_row(dic, size, row_nr) -> list:
    row = [0] * (size + 1)
    s = 1
    for sensor, dist in dic.items():
        dist_row = distance_mh(sensor, (row_nr, sensor[1]))
        # als sensor is dichtbij genoeg, voeg # toe rondom dit (row_nr, sensor[1])
        min_afstand = dist - dist_row
        if min_afstand >= 0:
            l = max(sensor[1] - min_afstand, 0)
            r = min(sensor[1] + min_afstand, size)
            row[l : r + 1] = [1] * (r - l + 1)
            if row.count(0) == 0:
                s = 0
    return row, s


def compute_distances(dic):
    for sensor, beacon in dic.items():
        dist = distance_mh(sensor, beacon)
        dic[sensor] = dist
    return dic


def main(data, row_nr):
    dic = read(data)
    answer = compute_answer(dic, row_nr)
    return answer.count("#")


def main2(data, size):
    dic = read(data)
    dic = compute_distances(dic)
    for row_nr in range(size + 1):
        if row_nr % 1000 == 0:
            print(row_nr)
        row, count = do_one_row(dic, size, row_nr)
        if count == 1:
            x = row.index(0)
            break
    return 4000000 * row_nr + x


# part 1
# print(main(TEST, 10))
# print(main(DATA, 2000000))

# part 2
n = 100
start = time.time()
for i in range(n):
    print(main2(TEST, 20))
print(round((time.time() - start) / n, 5))
print(main2(DATA, 400000))


# %%
data = DATA
sensors = (
    (
        int(line.split(" ")[2].split("=")[1].strip(",")),
        int(line.split(" ")[3].split("=")[1].strip(":")),
        int(line.split(" ")[8].split("=")[1].strip(",")),
        int(line.split(" ")[9].split("=")[1].strip(",")),
    )
    for line in data
)
sensor_dist = ((x, y, (abs(x - xb) + abs(y - yb))) for x, y, xb, yb in sensors)

squares = []
for x, y, d in sensor_dist:
    rx = x + d
    lx = x - d
    ru = rx - y
    rv = rx + y
    lu = lx - y
    lv = lx + y
    squares.append((ru, rv, lu, lv))

u_vals = set(ru for ru, _, _, _ in squares) | set(lu for _, _, lu, _ in squares)

to_add = set()

for u_val in u_vals:
    to_add.add(u_val + 1)
    to_add.add(u_val - 1)

u_vals |= to_add

u_vals = sorted(u_vals)

u_ranges = {key: [] for key in u_vals}
for index, (ru, rv, lu, lv) in enumerate(squares):
    for u_k in u_vals:
        if ru > lu:
            if lu <= u_k <= ru:
                u_ranges[u_k].append(index)
        else:
            if ru <= u_k <= ru:
                u_ranges[u_k].append(index)

v_ranges = {}

for u, sqs in u_ranges.items():
    ranges = []
    for sq in sqs:
        ru, rv, lu, lv = squares[sq]
        if rv > lv:
            rng = [lv, rv]
        else:
            rng = [rv, lv]
        ranges.append(rng)
    ranges.sort()
    stack = []
    if len(ranges) > 0:
        stack.append(ranges[0])
        for r in ranges[1:]:
            if stack[-1][0] <= r[0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], r[1])
            else:
                stack.append(r)
    v_ranges[u] = stack

for u, v_range in v_ranges.items():
    if len(v_range) == 2:
        v = v_range[0][1] + 1
        x = int(u / 2 + v / 2)
        y = int(v / 2 - u / 2)
        print(x * 4000000 + y)
        break

# %%
