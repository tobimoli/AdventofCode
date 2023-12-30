import numpy as np

with open("input.txt") as f:
    data = f.read().split("\n")


def compute_info(data, divider, part=1):
    info = []
    for line in data:
        pos, vel = line.split("@")
        px, py, pz = pos.split(",")
        vx, vy, vz = vel.split(",")
        if part == 1:
            info.append(
                [
                    np.array([int(px) / divider, int(py) / divider, int(pz) / divider]),
                    np.array([int(vx), int(vy), int(vz)]),
                ]
            )
        else:
            info.append((int(px), int(py), int(pz), int(vx), int(vy), int(vz)))
    return info


def line_intersection(line1, line2, vel1, vel2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return False

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if is_in_area(x, y):
        if is_in_future(x, y, xdiff, ydiff, line1, 0):
            if is_in_future(x, y, xdiff, ydiff, line2, 1):
                return True
    return False


def is_in_future(x, y, xdiff, ydiff, line, line_nr):
    if (xdiff[line_nr] >= 0) and (x <= line[0][0]):
        if (ydiff[line_nr] >= 0) and (y <= line[0][1]):
            return True
        elif (ydiff[line_nr] < 0) and (y > line[0][1]):
            return True
        else:
            return False
    elif (xdiff[line_nr] < 0) and (x > line[0][0]):
        if (ydiff[line_nr] >= 0) and (y <= line[0][1]):
            return True
        elif (ydiff[line_nr] < 0) and (y > line[0][1]):
            return True
        else:
            return False
    return False


def is_in_area(x, y):
    if test_area[0] <= x <= test_area[1]:
        if test_area[0] <= y <= test_area[1]:
            return True
    return False


def intersect(line1, line2, part=1) -> bool:
    pos1, vel1 = line1
    pos2, vel2 = line2

    if part == 1:
        pos1 = pos1[:2]
        pos2 = pos2[:2]
        vel1 = vel1[:2]
        vel2 = vel2[:2]

    # parallel
    div = vel2 / vel1
    if all(div == div[0]):
        return False

    pos1b = pos1 + vel1
    pos2b = pos2 + vel2

    return line_intersection((pos1, pos1b), (pos2, pos2b), vel1, vel2)


# part 1
divider = 1_000_000

test_area = (200000000000000 / divider, 400000000000000 / divider)
som = 0
info = compute_info(data, divider)
for line_nr, line1 in enumerate(info[:-1]):
    for line2 in info[(line_nr + 1) :]:
        som += intersect(line1, line2)
print(som)

# part 2
import itertools as it

InputList = compute_info(data, 0, 2)

# PX1 + VX1*t = PX2 + VX2*t
# PX1 - PX2 = VX2*t - VX1*t
# (PX1-PX2)/(VX2-VX1) = t

PotentialXSet = None
PotentialYSet = None
PotentialZSet = None
for A, B in it.combinations(InputList, 2):
    APX, APY, APZ, AVX, AVY, AVZ = A
    BPX, BPY, BPZ, BVX, BVY, BVZ = B

    if AVX == BVX and abs(AVX) > 100:
        NewXSet = set()
        Difference = BPX - APX
        for v in range(-1000, 1000):
            if v == AVX:
                continue
            if Difference % (v - AVX) == 0:
                NewXSet.add(v)
        if PotentialXSet != None:
            PotentialXSet = PotentialXSet & NewXSet
        else:
            PotentialXSet = NewXSet.copy()
    if AVY == BVY and abs(AVY) > 100:
        NewYSet = set()
        Difference = BPY - APY
        for v in range(-1000, 1000):
            if v == AVY:
                continue
            if Difference % (v - AVY) == 0:
                NewYSet.add(v)
        if PotentialYSet != None:
            PotentialYSet = PotentialYSet & NewYSet
        else:
            PotentialYSet = NewYSet.copy()
    if AVZ == BVZ and abs(AVZ) > 100:
        NewZSet = set()
        Difference = BPZ - APZ
        for v in range(-1000, 1000):
            if v == AVZ:
                continue
            if Difference % (v - AVZ) == 0:
                NewZSet.add(v)
        if PotentialZSet != None:
            PotentialZSet = PotentialZSet & NewZSet
        else:
            PotentialZSet = NewZSet.copy()

print(PotentialXSet, PotentialYSet, PotentialZSet)
RVX, RVY, RVZ = PotentialXSet.pop(), PotentialYSet.pop(), PotentialZSet.pop()

APX, APY, APZ, AVX, AVY, AVZ = InputList[0]
BPX, BPY, BPZ, BVX, BVY, BVZ = InputList[1]
MA = (AVY - RVY) / (AVX - RVX)
MB = (BVY - RVY) / (BVX - RVX)
CA = APY - (MA * APX)
CB = BPY - (MB * BPX)
XPos = int((CB - CA) / (MA - MB))
YPos = int(MA * XPos + CA)
Time = (XPos - APX) // (AVX - RVX)
ZPos = APZ + (AVZ - RVZ) * Time

print(XPos, YPos, ZPos)
Part2Answer = XPos + YPos + ZPos

print(f"{Part2Answer = }")
