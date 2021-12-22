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
    if x1 == x2:
        if y2>y1:
            sign = 1
        else:
            sign = -1
        for y in range(int(y1), int(y2) + sign*1, sign*1):
            field[int(x1), y] += 1
    elif y1 == y2:
        if x2>x1:
            sign = 1
        else:
            sign = -1
        for x in range(int(x1), int(x2) + sign*1, sign*1):
            field[x, int(y1)] += 1

answer = np.sum(field >= 2)
print(answer)
#6007