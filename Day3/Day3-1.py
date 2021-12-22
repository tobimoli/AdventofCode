import numpy as np
filename = 'input_day3.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=str)
size = len(data)

sum = np.zeros(len(data[0]))

def bin_to_dec(bin_number):
    dec_number = 0
    l = len(str(bin_number))
    for i,j in enumerate(str(bin_number)):
        dec_number += int(j) * 2**(l - i - 1)
    return dec_number

for number in data:
    for ind, num in enumerate(number):
        sum[ind] += int(num)

eps = ''
gam = ''
for s in sum:
    if s<size//2:
        eps += '1'
        gam += '0'
    else:
        eps += '0'
        gam += '1'

EPS = bin_to_dec(eps)
GAM = bin_to_dec(gam)

print(EPS*GAM)