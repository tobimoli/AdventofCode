import numpy as np
filename = 'input_day9.txt'
input = np.loadtxt(filename, skiprows=0, dtype=str)
#input = ['2199943210','3987894921','9856789892','8767896789','9899965678']

size = len(input)
arr = np.zeros(shape = (size, len(input[0])))
for i, line in enumerate(input):
    arr[i] = np.array([int(num) for num in line])

def adjacent(array, row_nr, col_nr):
    nr_rows, nr_cols = array.shape
    if row_nr == 0 and col_nr == 0:
        adj = [(row_nr+1,col_nr,array[row_nr+1, col_nr]), (row_nr,col_nr+1,array[row_nr, col_nr+1])]
    elif row_nr == 0 and col_nr == nr_cols-1:
        adj = [(row_nr+1,col_nr,array[row_nr+1, col_nr]), (row_nr,col_nr-1,array[row_nr, col_nr-1])]
    elif row_nr == 0:
        adj = [(row_nr+1,col_nr,array[row_nr+1, col_nr]), (row_nr,col_nr+1,array[row_nr, col_nr+1]), (row_nr,col_nr-1,array[row_nr, col_nr-1])]
    elif row_nr == nr_rows-1 and col_nr == 0:
        adj = [(row_nr-1,col_nr,array[row_nr-1, col_nr]), (row_nr,col_nr+1,array[row_nr, col_nr+1])]
    elif row_nr == nr_rows-1 and col_nr == nr_cols-1:
        adj = [(row_nr-1,col_nr,array[row_nr-1, col_nr]), (row_nr,col_nr-1,array[row_nr, col_nr-1])]
    elif row_nr == nr_rows-1:
        adj = [(row_nr-1,col_nr,array[row_nr-1, col_nr]), (row_nr,col_nr+1,array[row_nr, col_nr+1]), (row_nr,col_nr-1,array[row_nr, col_nr-1])]
    elif col_nr == 0:
        adj = [(row_nr+1,col_nr,array[row_nr+1, col_nr]), (row_nr-1,col_nr,array[row_nr-1, col_nr]), (row_nr,col_nr+1,array[row_nr, col_nr+1])]
    elif col_nr == nr_cols-1:
        adj = [(row_nr+1,col_nr,array[row_nr+1, col_nr]), (row_nr-1,col_nr,array[row_nr-1, col_nr]), (row_nr,col_nr-1,array[row_nr, col_nr-1])]
    else:
        adj = [(row_nr+1,col_nr,array[row_nr+1, col_nr]), (row_nr-1,col_nr,array[row_nr-1, col_nr]), (row_nr,col_nr+1,array[row_nr, col_nr+1]), (row_nr,col_nr-1,array[row_nr, col_nr-1])]
    return adj

def low_points(array, row_nr, col_nr):
    value = array[row_nr, col_nr]
    adj = adjacent(array, row_nr, col_nr)
    if np.all(value < np.array(adj)[:,2]):
        return True
    else:
        return False

LOW_POINTS = []
for row, val_row in enumerate(arr):
    for col, val in enumerate(val_row):
        if low_points(arr, row, col):
            LOW_POINTS.append((row,col,val))

BASINS = {}
for nr, low_point in enumerate(LOW_POINTS):
    basin = [low_point]
    bas_full = False
    i = 0
    while not bas_full:
        checker = basin[i]
        adj = adjacent(arr, checker[0], checker[1])
        for ad in adj:
            if ad[2]<9 and ad[2]>low_point[2] and ad not in basin:
                basin.append(ad)
        if checker == basin[-1]:
            bas_full = True
        i+=1

    BASINS[nr] = basin

sizes = []
for basin in BASINS.values():
    sizes.append(len(basin))

sizes.sort()
lar3 = sizes[-3:]
answer = lar3[0]*lar3[1]*lar3[2]
print(answer)