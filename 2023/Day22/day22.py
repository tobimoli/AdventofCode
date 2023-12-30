import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n")
f.close()

n_bricks = len(data)

# read everything from data
bricks = []
for brick in data:
    s, e = brick.split("~")

    s = np.array([int(i) for i in s.split(",")])
    e = np.array([int(i) for i in e.split(",")])
    bricks.append([s, e])

# maak de kaart
max_x, max_y, max_z = 0, 0, 0
for brick in bricks:
    for b in brick:
        if b[0] > max_x:
            max_x = b[0]
    for b in brick:
        if b[1] > max_y:
            max_y = b[1]
    for b in brick:
        if b[2] > max_z:
            max_z = b[2]
kaart = np.zeros((max_x + 1, max_y + 1, max_z + 1), dtype=int)

bricks.sort(key=lambda x: x[0][2])

# vul kaart in met stenen
for nr, brick in enumerate(bricks):
    if all(brick[0] == brick[1]):
        kaart[tuple(brick[0])] = nr + 1
        continue
    xyz = np.where((brick[1] - brick[0]) != 0)[0][0]
    if brick[0][xyz] <= brick[1][xyz]:
        l, r = brick[0], brick[1]
    else:
        l, r = brick[1], brick[0]
    for x in range(l[xyz], r[xyz] + 1):
        if xyz == 0:
            kaart[x, l[1], l[2]] = nr + 1
        elif xyz == 1:
            kaart[l[0], x, l[2]] = nr + 1
        else:
            kaart[l[0], l[1], x] = nr + 1

# laat stenen vallen
for nr in range(len(bricks)):
    blocks = np.argwhere(kaart == (nr + 1))
    i = 0
    if any([b[2] == 0 for b in blocks]):
        continue
    # hoeveel kan hij zakken?
    while all([(kaart[tuple(b - (i + 1) * np.array([0, 0, 1]))] == 0) or (kaart[tuple(b - (i + 1) * np.array([0, 0, 1]))] == nr + 1) for b in blocks]):
        i += 1
        if any([(b[2] - i) == 0 for b in blocks]):
            break
    if i > 0:
        for b in blocks:
            kaart[tuple(b)] = 0
            kaart[tuple(b - i * np.array([0, 0, 1]))] = nr + 1
        blocks = np.argwhere(kaart == (nr + 1))

# which block leans on which block
supports = {i: set() for i in range(1, len(bricks) + 1)}
for nr, brick in enumerate(bricks):
    blocks = np.argwhere(kaart == (nr + 1))
    for b in blocks:
        if b[2] == kaart.shape[2] - 1:
            continue
        bb = kaart[tuple(b + [0, 0, 1])]
        if (bb != 0) and (bb != (nr + 1)):
            supports[nr + 1].add(bb)

# welke steen kan je weghalen?
weghalen = []
all_supports = list(supports.values())
for brick, supporting in supports.items():
    if len(supporting) == 0:
        weghalen.append(brick)
        continue

    other_supports = [i for j, i in enumerate(all_supports) if j != brick - 1]
    a = set()
    for i in other_supports:
        a.update(i)
    if all([i in a for i in supporting]):
        weghalen.append(brick)

# part 1
print(len(weghalen))

# part 2
def bereken_aantal_vallen(nr):
    if len(supports[nr]) == 0:
        return 0
    vallenden = [nr]
    change = True
    while change:
        change = False
        other_supports = [i for j, i in enumerate(all_supports) if j + 1 not in vallenden]
        a = set()
        for i in other_supports:
            a.update(i)
        for q in vallenden:
            for i in supports[q]:
                if i not in a:
                    if i not in vallenden:
                        vallenden.append(i)
                        change = True

    return len(vallenden) - 1


som = 0
for brick in range(1, len(bricks) + 1):
    print(brick)
    som += bereken_aantal_vallen(brick)
print(som)
