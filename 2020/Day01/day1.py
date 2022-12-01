# %%
import os
import numpy as np
os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2020/Day01/')

f = open('input_day1.txt', 'r')
data = f.read().split('\n')
f.close()

# Part 1
for index1, number1 in enumerate(data):
    for index2, number2 in enumerate(data):
        if index1 < index2:
            if int(number1) + int(number2) == 2020:
                print(int(number1) * int(number2))

# Part 2
for index1, number1 in enumerate(data):
    for index2, number2 in enumerate(data):
        for index3, number3 in enumerate(data):
            if index1 < index2:
                if index2 < index3:
                    if int(number1) + int(number2) + int(number3) == 2020:
                        print(int(number1) * int(number2) * int(number3))