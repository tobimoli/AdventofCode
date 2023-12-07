file = "input"

f = open(f'{file}.txt', 'r')
data = f.read().split('\n')
f.close()


# part 1
som = 0
for measures in data:
    l, w, h = [int(i) for i in measures.split("x")]

    area = 2*l*w + 2*w*h + 2*h*l
    extra = min(l*w, l*h, w*h)
    total_area = area + extra
    som += total_area
print(som)

# part 2
som = 0
for measures in data:
    l, w, h = [int(i) for i in measures.split("x")]

    lst = [l, w, h]
    lst.sort()

    bow = l * w * h
    box = 2 * min(lst) + 2 * lst[1]
    som += bow + box
print(som)