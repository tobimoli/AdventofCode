import numpy as np
filename = 'input_day5.txt'
lines = np.loadtxt(filename, delimiter='/n', skiprows=0, dtype=str)

data = np.zeros((len(lines), 4))

for line_nr, line in enumerate(lines):
    values = line.split(' -> ')
    [x1, y1] = values[0].split(',')
    [x2, y2] = values[1].split(',')
    data[line_nr,:] = x1, y1, x2, y2

size = int(np.max(data))
field = np.zeros((size+1, size+1))

for line in data:
    x1, y1, x2, y2 = line
    sign_x, sign_y = 1, 1
    if y1 > y2:
        sign_y = -1
    if x1 > x2:
        sign_x = -1
    xlst = list(range(int(x1), int(x2) + sign_x, sign_x))
    ylst = list(range(int(y1), int(y2) + sign_y, sign_y))
    field[xlst, ylst] += 1

answer = np.sum(field >= 2)
print(answer)
#19349