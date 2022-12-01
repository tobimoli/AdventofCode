# %%
import os
import numpy as np
os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day1/')

f = open('input_day1.txt', 'r')
data = f.read().split('\n')
f.close()

elvesCalories = np.zeros(len(data))
elfNumber = 0
for calories in data:
    if calories == '':
        elfNumber += 1
    else:
        elvesCalories[elfNumber] += int(calories)

        
# Part 1
print(max(elvesCalories))

# Part 2
print(sum(sorted(elvesCalories)[-3:]))