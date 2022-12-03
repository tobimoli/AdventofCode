# %%
import os
import re
import numpy as np
os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2020/Day06/')

with open('input_day6.txt', 'r') as f:
    data = f.read().split('\n')

group_nr = 0
group_forms = {}
for form in data:
    if form == '':
        group_nr += 1
    else:
        if group_nr in group_forms:
            group_forms[group_nr] += [form]
        else:
            group_forms[group_nr] = [form]

# part 1
som = 0
for _, answers in group_forms.items():
    concatenation = ''
    for answer in answers:
        concatenation += answer
    som += len(set(concatenation))
print(som)

# part 2
som = 0
for _, answers in group_forms.items():
    answers = [set(answer) for answer in answers]
    intersection = set.intersection(*answers)
    som += len(intersection)
print(som)