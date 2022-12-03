# %%
import os
import re
import numpy as np
os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2020/Day05/')

with open('input_day5.txt', 'r') as f:
    data = f.read().split('\n')

def compute_seatid(row, column):
    return row * 8 + column

def binary_to_decimal(binary, zero, one):
    binary = binary.replace(zero, '0')
    binary = binary.replace(one, '1')

    som = 0
    for power, i in enumerate(binary[::-1]):
        som += int(i) * 2**(power)
    return som

seatids = np.zeros(len(data))
for i, boarding_pass in enumerate(data):
    row_binary = boarding_pass[:7]
    col_binary = boarding_pass[7:]
    row_decimal = binary_to_decimal(row_binary, 'F', 'B')
    col_decimal = binary_to_decimal(col_binary, 'L', 'R')

    seatid = compute_seatid(row_decimal, col_decimal)
    seatids[i] = seatid

# part 1
print(max(seatids))

# part 2
max_seat_id = compute_seatid(2**(len(row_binary)) - 1, 2**(len(col_binary)) - 1)

for seat_id in range(max_seat_id):
    if seat_id not in seatids:
        if seat_id - 1 in seatids:
            if seat_id + 1 in seatids:
                print(seat_id)