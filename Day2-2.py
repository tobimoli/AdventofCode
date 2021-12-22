import numpy as np
filename = 'input_day2.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=str)

x = 0
d = 0
a = 0
for dat in data:
    if dat[:-2] == 'down':
        a += int(dat[5:])
    elif dat[:-2] == 'up':
        a -= int(dat[3:])
    elif dat[:-2] == 'forward':
        x += int(dat[8:])
        d += a * int(dat[8:])
    else:
        print('input is not correct')

print(x*d)


