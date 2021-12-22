import numpy as np
filename = 'input_day9.txt'
input = np.loadtxt(filename, delimiter='', skiprows=0, dtype=str)
size = len(input)

arr = np.zeros(shape = (size, len(input[0])))
for i, line in enumerate(input):
    arr[i] = np.array([int(num) for num in line])

def adjacent(array, row_nr, col_nr):
    nr_rows, nr_cols = array.shape
    if row_nr == 0 and col_nr == 0:
        adj = [array[row_nr+1, col_nr], array[row_nr, col_nr+1]]
    elif row_nr == 0 and col_nr == nr_cols-1:
        adj = [array[row_nr+1, col_nr], array[row_nr, col_nr-1]]
    elif row_nr == 0:
        adj = [array[row_nr+1, col_nr], array[row_nr, col_nr+1], array[row_nr, col_nr-1]]
    elif row_nr == nr_rows-1 and col_nr == 0:
        adj = [array[row_nr-1, col_nr], array[row_nr, col_nr+1]]
    elif row_nr == nr_rows-1 and col_nr == nr_cols-1:
        adj = [array[row_nr-1, col_nr], array[row_nr, col_nr-1]]
    elif row_nr == nr_rows-1:
        adj = [array[row_nr-1, col_nr], array[row_nr, col_nr+1], array[row_nr, col_nr-1]]
    elif col_nr == 0:
        adj = [array[row_nr+1, col_nr], array[row_nr-1, col_nr], array[row_nr, col_nr+1]]
    elif col_nr == nr_cols-1:
        adj = [array[row_nr+1, col_nr], array[row_nr-1, col_nr], array[row_nr, col_nr-1]]
    else:
        adj = [array[row_nr+1, col_nr], array[row_nr-1, col_nr], array[row_nr, col_nr+1], array[row_nr, col_nr-1]]
    return adj

def low_points(array, row_nr, col_nr):
    value = array[row_nr, col_nr]
    adj = adjacent(array, row_nr, col_nr)
    if np.all(value < np.array(adj)):
        return True
    else:
        return False


LOW_POINTS = []
for row, val_row in enumerate(arr):
    for col, val in enumerate(val_row):
        if low_points(arr, row, col):
            LOW_POINTS.append(val)

answer = sum(LOW_POINTS) + len(LOW_POINTS)
print(answer)