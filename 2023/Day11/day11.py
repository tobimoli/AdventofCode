import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n")
f.close()
data = np.array([[j for j in i] for i in data])

# maak grid met unieke getallen voor galaxies
n_galaxies = np.sum(data == "#")

data[data == "."] = 0
data[data == "#"] = 1
data = data.astype(int)
data[data == 1] = [i for i in range(1, n_galaxies + 1)]

# expand universe
empty_rows = np.array(np.where(np.sum(data, axis=1) == 0)[0])
empty_cols = np.array(np.where(np.sum(data, axis=0) == 0)[0])


# bereken afstand tussen alle galaxies
def compute_distance(gal1, gal2, expension=2):
    row1, col1 = np.where(data == gal1)
    row2, col2 = np.where(data == gal2)

    if row1 <= row2:
        aantal_empty_rows = np.sum((empty_rows > row1[0]) & (empty_rows < row2[0]))
    else:
        aantal_empty_rows = np.sum((empty_rows < row1[0]) & (empty_rows > row2[0]))
    if col1 <= col2:
        aantal_empty_cols = np.sum((empty_cols > col1[0]) & (empty_cols < col2[0]))
    else:
        aantal_empty_cols = np.sum((empty_cols < col1[0]) & (empty_cols > col2[0]))

    afstand = abs(row1[0] - row2[0])
    afstand += abs(col1[0] - col2[0])

    afstand += (expension - 1) * (aantal_empty_cols + aantal_empty_rows)
    return afstand


# part 1
tot_afstand = 0
for galaxy1 in range(1, n_galaxies + 1):
    for galaxy2 in range(galaxy1 + 1, n_galaxies + 1):
        tot_afstand += compute_distance(galaxy1, galaxy2)

print(tot_afstand)

# part 2
# expanding n times, so don't make the array bigger, but count 'on the way'
tot_afstand = 0
for galaxy1 in range(1, n_galaxies + 1):
    for galaxy2 in range(galaxy1 + 1, n_galaxies + 1):
        tot_afstand += compute_distance(galaxy1, galaxy2, expension=1_000_000)

print(tot_afstand)
