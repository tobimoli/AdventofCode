import numpy as np
filename = 'input_day3.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=str)

size = len(data)
oxy = data.copy()
co2 = data.copy()
Sum = np.zeros(len(data[0]))

def bin_to_dec(bin_number):
    dec_number = 0
    l = len(str(bin_number))
    for i,j in enumerate(str(bin_number)):
        dec_number += int(j) * 2**(l - i - 1)
    return dec_number

def most_common(list, index):
    #find the most common value at specified index in the list
    total = [int(x[index]) for x in list]
    ones = np.sum(total)
    zeroes = len(list) - ones
    if ones > zeroes:
        return '1'
    elif ones < zeroes:
        return '0'
    else:
        return 'equal'

ind = 0
while len(oxy) > 1:
    common = most_common(oxy, ind)
    print(ind, len(oxy), common)
    if common == 'equal':
        common = '1'
    oxy = [i for i in oxy if i[ind] == common]
    ind +=1
ind = 0
while len(co2) > 1:
    common = most_common(co2, ind)
    print(ind, len(co2), common)
    if common == 'equal':
        common = '0'
    elif common == '1':
        common = '0'
    elif common == '0':
        common = '1'
    co2 = [i for i in co2 if i[ind] == common]
    ind +=1

OXY = bin_to_dec(oxy[0])
CO2 = bin_to_dec(co2[0])
print(OXY*CO2)