import numpy as np
filename = 'input_day7.txt'
input = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=int)
#input = np.array([16,1,2,0,4,2,7,1,2,14])

def SUM(number):
    total = 0
    number = int(number)
    for num in range(number+1):
        total += num
    return total

max_input = np.max(input)
fuels = np.zeros(max_input)

for val in range(max_input):
    print(val)
    distance = np.abs(input - val)
    fuel = 0
    for dist in distance:
        fuel += SUM(dist)
    fuels[val] = fuel

print(np.argmin(fuels))
print(np.min(fuels))