import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n")
f.close()

data = np.array([[j for j in i] for i in data])
size = data.shape[0]

start = np.where(data == "S")
start = start[0][0], start[1][0]

def compute_n_positions(n_steps):
    positions = {start}
    kaart = {}
    for i in range(n_steps):
        new_positions = set()
        for pos in positions:
            if pos in kaart:
                new_positions.update(kaart[pos])
            else:
                kaart[pos] = set()
                for step in [[1,0],[-1,0],[0,1],[0,-1]]:
                    new_pos = tuple(np.array(pos) + step)
                    look_pos = np.array(pos) + step
                    look_pos %= size
                    if data[tuple(look_pos)] != "#":
                        kaart[pos].add(new_pos)
                        new_positions.add(new_pos)
        positions = new_positions
    return len(positions)

# part 1
print(compute_n_positions(64))

# part 2
steps = 26501365
residual = 26501365 % size


# polynomial extrapolation
a0 = compute_n_positions(residual)
a1 = compute_n_positions(residual + size)
a2 = compute_n_positions(residual + 2 * size)

matrix = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
b = np.array([a0, a1, a2])
x = np.linalg.solve(matrix, b).astype(int)

# note that 26501365 = 202300 * 131 + 65 where 131 is the dimension of the grid
n = (steps - residual) // size

