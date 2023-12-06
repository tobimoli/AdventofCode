f = open("input_day6.txt", "r")
data = f.read().split("\n")
f.close()

times = [int(i) for i in data[0].split(":")[1].split()]
dists = [int(i) for i in data[1].split(":")[1].split()]


def compute_ways_to_win_one_race(time, dist):
    ways_to_win_race = 0
    for hold_sec in range(time):
        distance = (hold_sec * 1) * (time - hold_sec)

        if distance > dist:
            ways_to_win_race += 1
    return ways_to_win_race


# part 1
ways_to_win = []

for race in range(len(times)):
    time = times[race]
    dist = dists[race]
    ways_to_win_race = compute_ways_to_win_one_race(time, dist)
    ways_to_win.append(ways_to_win_race)
print(ways_to_win)

product = 1
for i in ways_to_win:
    product *= i
print(product)


# part 2
time = int(data[0].split(":")[1].replace(" ", ""))
dist = int(data[1].split(":")[1].replace(" ", ""))

print(compute_ways_to_win_one_race(time, dist))
