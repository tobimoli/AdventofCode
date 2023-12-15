import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n")
f.close()

data = np.array([[j for j in i] for i in data])
n_rows, n_cols = data.shape


def tilt(df, direction):
    if direction == "N":
        tilting = True
        while tilting:
            tilting = False
            for row_nr in range(n_rows):
                for col_nr in range(n_cols):
                    item = df[row_nr, col_nr]
                    if item == "O":
                        if row_nr > 0:
                            item_above = df[row_nr - 1, col_nr]
                            if item_above == ".":
                                tilting = True
                                df[row_nr, col_nr] = "."
                                df[row_nr - 1, col_nr] = "O"
    elif direction == "S":
        tilting = True
        while tilting:
            tilting = False
            for row_nr in range(n_rows):
                for col_nr in range(n_cols):
                    item = df[row_nr, col_nr]
                    if item == "O":
                        if row_nr < (n_rows - 1):
                            item_above = df[row_nr + 1, col_nr]
                            if item_above == ".":
                                tilting = True
                                df[row_nr, col_nr] = "."
                                df[row_nr + 1, col_nr] = "O"
    elif direction == "E":
        tilting = True
        while tilting:
            tilting = False
            for row_nr in range(n_rows):
                for col_nr in range(n_cols):
                    item = df[row_nr, col_nr]
                    if item == "O":
                        if col_nr < (n_cols - 1):
                            item_above = df[row_nr, col_nr + 1]
                            if item_above == ".":
                                tilting = True
                                df[row_nr, col_nr] = "."
                                df[row_nr, col_nr + 1] = "O"
    elif direction == "W":
        tilting = True
        while tilting:
            tilting = False
            for row_nr in range(n_rows):
                for col_nr in range(n_cols):
                    item = df[row_nr, col_nr]
                    if item == "O":
                        if col_nr > 0:
                            item_above = df[row_nr, col_nr - 1]
                            if item_above == ".":
                                tilting = True
                                df[row_nr, col_nr] = "."
                                df[row_nr, col_nr - 1] = "O"
    return df


data1 = tilt(data.copy(), "N")

# compute score
score = 0
for i, row in enumerate(data1):
    score += (row == "O").sum() * (n_rows - i)
print(score)


# part 2
def cycle(df):
    df = tilt(df.copy(), "N")
    df = tilt(df.copy(), "W")
    df = tilt(df.copy(), "S")
    df = tilt(df.copy(), "E")
    return df


data_loop = data.copy()
lst_cycles = [data_loop]

cycle_found = False
cycles = 1_000_000_000
for loop in range(cycles):
    print(loop)
    data_loop = cycle(data_loop.copy())
    for nr, i in enumerate(lst_cycles):
        if np.all(i == data_loop):
            print("hier")
            index_found = nr
            cycle_found = True
            break
    if cycle_found:
        break
    lst_cycles.append(data_loop)

print(len(lst_cycles), index_found)
length_cycle = len(lst_cycles) - index_found

remainder = (cycles - index_found) % length_cycle

for loop in range(remainder):
    data_loop = cycle(data_loop.copy())

# compute score
score = 0
for i, row in enumerate(data_loop):
    score += (row == "O").sum() * (n_rows - i)
print(score)
