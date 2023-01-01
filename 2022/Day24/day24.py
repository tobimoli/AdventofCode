# %%
import re

import numpy as np

DAY = str(24)

# os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")


def find_start(data):
    toprow = 0
    column = data[toprow].index(".")
    return (toprow, column)


def get_initial_blizzards(data):
    blizzards = []
    for idx, row in enumerate(data):
        for idy, direction in enumerate(row):
            if is_blizzard(direction):
                blizzards.append((idx, idy, direction))
    return blizzards


def is_blizzard(item):
    if item == ".":
        return False
    elif item == "#":
        return False
    elif item == "E":
        return False
    else:
        return True


def get_next_blizzards(old_blizzards):
    new_blizzards = []
    for blizzard in old_blizzards:
        new_idx, new_idy = move_blizzard(blizzard)
        new_blizzards.append((new_idx, new_idy, blizzard[2]))
    return new_blizzards


def move_blizzard(blizzard):
    idx, idy, direction = blizzard
    onder, rechts, boven, links = ONDER, RECHTS, 0, 0
    new_idx, new_idy = idx, idy
    # pas de beweging toe
    if direction == ">":
        new_idy += 1
    elif direction == "<":
        new_idy -= 1
    elif direction == "^":
        new_idx -= 1
    elif direction == "v":
        new_idx += 1
    # kijk of het op de rand zit, zo ja pas aan, zo nee dan niet.
    if new_idx == boven:
        new_idx = onder - 1
    elif new_idx == onder:
        new_idx = boven + 1
    elif new_idy == rechts:
        new_idy = links + 1
    elif new_idy == links:
        new_idy = rechts - 1
    return new_idx, new_idy


def get_possible_moves(blizzards, position, grid):
    grid_size = [len(grid), len(grid[0])]
    possible_moves = []
    blizzard_locations = [(i[0], i[1]) for i in blizzards]
    steps = [(0, 1), (-1, 0), (0, -1), (1, 0), (0, 0)]
    check_positions = [tuple(x + y for x, y in zip(position, step)) for step in steps]
    for check_position in check_positions:
        if check_position not in blizzard_locations:
            x, y = check_position
            if (x >= 0) and (x < grid_size[0]) & (y >= 0) & (y < grid_size[1]):
                if grid[x][y] != "#":
                    possible_moves.append(check_position)
    return possible_moves


def find_end(data):
    lastrow = len(data) - 1
    column = data[lastrow].index(".")
    return lastrow, column


def reached_end(end, positions):
    if end in positions:
        return True
    return False


def simulation(data):
    # initial values
    start = find_start(data)
    end = find_end(data)
    blizzards = get_initial_blizzards(data)

    # do simulation
    blizzards, step1 = simulate(start, end, data, blizzards)
    print(step1)
    blizzards, step2 = simulate(end, start, data, blizzards)
    print(step2)
    blizzards, step3 = simulate(start, end, data, blizzards)
    print(step3)

    return step1 + step2 + step3


def simulate(start, end, empty_grid, blizzards, step=0):
    positions = [start]
    while not reached_end(end, positions):
        blizzards = get_next_blizzards(blizzards)
        new_positions = []
        for position in positions:
            new_positions += get_possible_moves(blizzards, position, empty_grid)
        positions = set(new_positions)

        step += 1
    return blizzards, step


def main(data):
    answer = simulation(data)
    return answer


data = DATA

ONDER, RECHTS = len(data) - 1, len(data[0]) - 1
print(main(data))

# %%
