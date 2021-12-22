import numpy as np
filename = 'input_day11.txt'
input = np.loadtxt(filename, dtype=int)
#input = np.array([5483143223,2745854711,5264556173,6141336146,6357385478,4167524645,2176841721,6882881134,4846848554,5283751526])
size = len(input)

arr = np.zeros(shape = (size, len(str(input[0]))))
for i, line in enumerate(input):
    arr[i] = np.array([int(num) for num in str(line)])

def flashing(arr, row, col):
    n_arr = arr.copy()
    n_arr[max(row-1,0) : min(row+2, size), max(col-1,0) : min(col+2, size)] += 1
    return n_arr

STEPS = 100
old_arr = arr
nr_flashes = 0
for step in range(STEPS):
    new_arr = old_arr + 1
    flashers = []
    for row, line in enumerate(new_arr):
        for col, value in enumerate(line):
            if value == 10:
                flashers.append((row,col))
    i = 0
    if len(flashers) == 0:
        done = True
    else:
        done = False
    while not done:
        (r,c) = flashers[i]
        new_arr = flashing(new_arr, r,c)

        for row, line in enumerate(new_arr):
            for col, value in enumerate(line):
                if value == 10 and (row, col) not in flashers:
                    flashers.append((row,col))
        if (r,c) == flashers[-1]:
            done = True
        i+=1
    for row, line in enumerate(new_arr):
        for col, value in enumerate(line):
            if value >= 10:
                new_arr[row,col] = 0
                nr_flashes += 1
    old_arr = new_arr

print(nr_flashes)