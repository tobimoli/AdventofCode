import numpy as np

f = open("input_day.txt", "r")
data = f.read().strip("\n")
f.close()

# data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def hash(s):
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value = value % 256
    return value


data = data.split(",")

# part 1
som = 0
for g in data:
    current = hash(g)
    som += current
print(som)

# part 2
boxes = [{} for _ in range(256)]

for g in data:
    if "-" in g:
        label = g.split("-")[0]
    else:
        label = g.split("=")[0]
    box = boxes[hash(label)]
    if '=' in g: 
        box[label] = int(g.split('=')[1])
    else: 
        box.pop(label, None)

print(sum((k+1)*(i+1)*v 
            for k, v in enumerate(boxes) 
            for i, v in enumerate(v.values())))