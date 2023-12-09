import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n")
f.close()

piramides = []
for row in data:
    diff = [int(i) for i in row.split(" ")]
    
    diffs = [diff]
    while any([i != 0 for i in diff]):
        diff = list(np.array(diff[1:]) - np.array(diff[:-1]))
        diffs.append(diff)
    piramides.append(diffs)

# part 1
som = 0
for piramide in piramides:  
    last_val = 0
    for row in piramide:
        last_val += row[-1]
    som += last_val
print(som)

# part 2
som = 0
for piramide in piramides:  
    last_val = 0
    plusmin = 1
    for row in piramide:
        last_val += row[0] * plusmin
        if plusmin == 1:
            plusmin = -1
        else:
            plusmin = 1
    som += last_val
print(som)