import numpy as np
filename = 'input_day7.txt'
input = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=int)
input = np.array([16,1,2,0,4,2,7,1,2,14])

max_input = np.max(input)
fuels = np.zeros(max_input)

for val in range(max_input):
    fuel = np.sum(np.abs(input - val))
    fuels[val] = fuel

print(np.argmin(fuels))
print(np.min(fuels))

