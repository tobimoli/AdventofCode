# %%
import re

import numpy as np

DAY = str(22)

# os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")

FACING = {"right": 0, "down": 1, "left": 2, "up": 3}
# FACING_INV = {v: k for k, v in FACING.items()}


def make_cube(data, s):
    lst = [[]] * 14
    lst[0] = [(0, c, FACING["down"]) for c in range(1 * s, 2 * s)]
    lst[1] = [(r, 0, FACING["right"]) for r in range(3 * s, 4 * s)]

    lst[2] = [(r, s, FACING["right"]) for r in range(1 * s)]
    lst[3] = [(r, 0, FACING["right"]) for r in reversed(range(2 * s, 3 * s))]

    lst[4] = [(r, s, FACING["right"]) for r in range(1 * s, 2 * s)]
    lst[5] = [(2 * s, c, FACING["down"]) for c in range(1 * s)]

    lst[6] = [(0, c, FACING["down"]) for c in range(2 * s, 3 * s)]
    lst[7] = [(4 * s - 1, c, FACING["up"]) for c in range(1 * s)]

    lst[8] = [(r, 3 * s - 1, FACING["left"]) for r in range(1 * s)]
    lst[9] = [(r, 2 * s - 1, FACING["left"]) for r in reversed(range(2 * s, 3 * s))]

    lst[10] = [(s - 1, c, FACING["up"]) for c in range(2 * s, 3 * s)]
    lst[11] = [(r, 2 * s - 1, FACING["left"]) for r in range(1 * s, 2 * s)]

    lst[12] = [(3 * s - 1, c, FACING["up"]) for c in range(1 * s, 2 * s)]
    lst[13] = [(r, s - 1, FACING["left"]) for r in range(3 * s, 4 * s)]

    dic = {}
    for i in range(len(lst)):
        face_new = lst[i][0][2]
        face_old = (face_new + 2) % 4
        key = [(r, c, face_old) for r, c, _ in lst[i]]
        if i % 2 == 0:
            dic.update(dict(zip(key, lst[i + 1])))
        else:
            dic.update(dict(zip(key, lst[i - 1])))
    return dic


def read_data(data):
    data1 = data[:-2]
    n_cols = max([len(line) for line in data1])
    grid = np.zeros((len(data1), n_cols))
    for row, line in enumerate(data1):
        for col, item in enumerate(line):
            if item == " ":
                continue
            elif item == ".":
                grid[row, col] = 1
            else:  #
                grid[row, col] = 2

    path = []
    data2 = data[-1]
    number = ""
    for i in data2:
        if i.isnumeric():
            number += i
        else:
            path.append(int(number))
            path.append(i)
            number = ""
    if number != "":
        path.append(int(number))
    return grid, path


def find_start_pos(grid):
    for row, line in enumerate(grid):
        for col, item in enumerate(line):
            if item == 1:
                return (row, col, FACING["right"])


def get_value_other_side(grid, position):
    row, col, face = position
    if PART2:
        d = make_cube(DATA, 50)
        if (row, col, face) in d:
            row, col, face = d[(row, col, face)]
        else:
            print("Wrong input")
    else:
        if face == FACING["right"]:
            col = np.where(grid[row, :] > 0)[0][0]
        elif face == FACING["left"]:
            col = np.where(grid[row, :] > 0)[0][-1]
        elif face == FACING["down"]:
            row = np.where(grid[:, col] > 0)[0][0]
        elif face == FACING["up"]:
            row = np.where(grid[:, col] > 0)[0][-1]
        else:
            print("Wrong face")
    return grid[row, col], (row, col, face)


def try_one_step(grid, position):
    row, col, face = position
    if face == FACING["right"]:
        new_pos_position = (row, col + 1, face)
    elif face == FACING["left"]:
        new_pos_position = (row, col - 1, face)
    elif face == FACING["up"]:
        new_pos_position = (row - 1, col, face)
    else:
        new_pos_position = (row + 1, col, face)
    new_row, new_col, face = new_pos_position
    max_row, max_col = grid.shape

    if (
        (new_row >= 0)
        and (new_row < max_row)
        and (new_col >= 0)
        and (new_col < max_col)
    ):
        if grid[new_row, new_col] == 1:
            return True, new_pos_position
        elif grid[new_row, new_col] == 2:
            return False, position
        else:
            value, new_pos_position = get_value_other_side(grid, position)
            if value == 2:
                return False, position
            else:
                return True, new_pos_position
    else:
        value, new_pos_position = get_value_other_side(grid, position)
        if value == 2:
            return False, position
        else:
            return True, new_pos_position


def move_steps(grid, position, steps):
    for _ in range(steps):
        possible, new_position = try_one_step(grid, position)
        if not possible:
            break
        else:
            position = new_position
    return position


def turn(position, leftright):
    row, col, face = position
    if leftright == "R":
        face = (face + 1) % 4
    else:
        face = (face - 1) % 4
    return (row, col, face)


def follow_path(grid, path):
    position = find_start_pos(grid)
    # print(grid, path)
    for item in path:
        # print(item, position)
        if isinstance(item, int):
            position = move_steps(grid, position, item)
        else:
            position = turn(position, item)
    return position


def main(data):
    grid, path = read_data(data)
    final_position = follow_path(grid, path)
    row, col, face = final_position
    return 1000 * (row + 1) + 4 * (col + 1) + face


# part 1
PART2 = False
print(main(TEST))
print(main(DATA))

# part 2
PART2 = True
print(main(DATA))

# %%
