import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n\n")
f.close()

data = [i.splitlines() for i in data]

def find_horizontal_mirror(puzzle, n_rows, n):
    for row_i in range(1, n_rows):
        # check if row_i can be the mirror
        rows_up = list(range(row_i))
        rows_down = list(range(row_i, n_rows))
        # even lang maken
        rows_up = rows_up[max(len(rows_up) - len(rows_down), 0):][::-1]
        rows_down = rows_down[:len(rows_up)]

        sum_refl = sum([sum([i != j for i,j in zip(puzzle[row_up_i], puzzle[row_down_i])]) for row_up_i, row_down_i in zip(rows_up, rows_down)])
        if sum_refl == n:
            return len(range(row_i))
    return 0

def find_mirror(puzzle, n):
    n_rows, n_cols = len(puzzle), len(puzzle[0])
    
    # horizontal mirror  
    mirror_found = find_horizontal_mirror(puzzle, n_rows, n)
    if mirror_found:
        return mirror_found, 0
    
    # vertical mirror
    transpose_puzzle = ["".join(x) for x in np.array([[i for i in line] for line in puzzle]).T.tolist()]
    mirror_found = find_horizontal_mirror(transpose_puzzle, n_cols, n)
    if mirror_found:
        return 0, mirror_found

for n in [0, 1]:
    ans = 0
    for puzzle in data:
        nr_rows, nr_cols = find_mirror(puzzle, n=n)
        ans += (nr_cols + 100 * nr_rows)
    print(ans)