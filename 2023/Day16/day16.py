import numpy as np

f = open("input_day.txt", "r")
data = f.read().replace("\\", "l").split("\n")
f.close()

data = np.array([[j for j in i] for i in data])
n_rows, n_cols = data.shape

# 0:>, 1:v, 2:<, 3:A

def get_new_loc(loc, dir):
    row, col = loc
    if dir == 0: # >
        col += 1
    elif dir == 1: # v
        row += 1
    elif dir == 2: # <
        col -= 1
    else: # A
        row -= 1
    return (row, col)

def get_new_dir(loc, dir):
    row, col = loc
    if data[row, col] == ".":
        new_dir = [dir]
    elif data[row, col] == "|":
        if dir in [0, 2]:
            new_dir = [1, 3]
        else:
            new_dir = [dir]
    elif data[row, col] == "-":
        if dir in [0, 2]:
            new_dir = [dir]
        else:
            new_dir = [0, 2]
    elif data[row, col] == "l": # \
        if dir == 0:
            new_dir = [1]
        elif dir == 1:
            new_dir = [0]
        elif dir == 2:
            new_dir = [3]
        else:
            new_dir = [2]
    else: # /
        if dir == 0:
            new_dir = [3]
        elif dir == 1:
            new_dir = [2]
        elif dir == 2:
            new_dir = [1]
        else:
            new_dir = [0]
    return new_dir

def get_n_energized_tiles(start):
    start_loc = list(start.keys())[0]
    start_dir = get_new_dir(start_loc, start[start_loc])
    
    energized_tiles = {}
    new_energized_tiles = {start_loc: start_dir}

    while len(new_energized_tiles) > 0:
        continue_beam = {}
        for loc, dir in new_energized_tiles.items():
            if loc in energized_tiles:
                for d in dir:
                    if d not in energized_tiles[loc]:
                        energized_tiles[loc].append(d)
                        if loc in continue_beam:
                            continue_beam[loc] += [d]
                        else:
                            continue_beam[loc] = [d]
            else:
                energized_tiles[loc] = dir
                continue_beam[loc] = dir
        new_energized_tiles = {}

        for loc, dirs in continue_beam.items():
            for dir in dirs:
                row, col = get_new_loc(loc, dir)
                if 0 <= col < n_cols:
                    if 0 <= row < n_rows:
                        new_dir = get_new_dir((row, col), dir)
                        if (row, col) in new_energized_tiles:
                            new_energized_tiles[(row, col)] += new_dir
                        else:
                            new_energized_tiles[(row, col)] = new_dir
    return len(energized_tiles)


# part 1
start = {(0, 0): 0} # row, column, direction(s)
print(get_n_energized_tiles(start))

# part 2
starts_1 = [{(i, 0): 0} for i in range(n_rows)]
starts_2 = [{(i, n_cols - 1): 2} for i in range(n_rows)]
starts_3 = [{(0, i): 1} for i in range(n_cols)]
starts_4 = [{(n_rows - 1, i): 3} for i in range(n_rows)]

starts = starts_1 + starts_2 + starts_3 + starts_4

maximum = 0
for start in starts:
    print(start)
    n = get_n_energized_tiles(start)
    if n > maximum:
        maximum = n

print(maximum)