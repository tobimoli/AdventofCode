import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n")
f.close()


def hexa2dec(hexa: str) -> int:
    dic = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    hexa_dic = dict(zip([str(i) for i in range(10)], list(range(10)))) | dic
    dec = sum([hexa_dic[i] * (16**j) for j, i in enumerate(hexa[::-1])])
    return dec


def compute_new_info(info):
    new_info = []
    movement = {0: "R", 1: "D", 2: "L", 3: "U"}
    for i in info:
        _, _, color = i.split(" ")
        move = movement[int(color[-2])]
        hexa = color[2:-2]
        dec = hexa2dec(hexa)

        new_info.append(f"{move} {dec} ()")
    return new_info


def find_points(info, loc):
    points = [loc]

    for dig in info:
        move, length, _ = dig.split(" ")
        length = int(length)

        if move == "U":
            d = [-1, 0]
        elif move == "D":
            d = [1, 0]
        elif move == "R":
            d = [0, 1]
        else:
            d = [0, -1]

        loc += np.array(d) * length
        points.append(loc.copy())
    return points


def det(a, b):
    xa, ya = a
    xb, yb = b
    return xa * yb - ya * xb


def shoelace(points, info):
    tot = 0
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        tot += det(p1, p2)

    area = abs(tot) // 2
    side = sum([int(i.split(" ")[1]) for i in info]) // 2 + 1
    return int(area + side)


# part 1
loc = np.array([0, 0], dtype="int64")
points = find_points(data, loc)
print(shoelace(points, data))


# part 2
info = compute_new_info(data)
loc = np.array([0, 0], dtype="int64")
points = find_points(info, loc)
print(shoelace(points, info))
