from math import gcd

f = open("input_day8.txt", "r")
data = f.read().split("\n")
f.close()

instructions = data[0]
maps = data[2:]

# make dictionary from maps
maps_d = {}
for i in maps:
    key, value = i.split(" = ")
    value = (value[1:4], value[6:-1])
    maps_d[key] = value


def do_one_step(leftright, position):
    if leftright == "R":
        position = maps_d[position][1]
    else:
        position = maps_d[position][0]
    return position


# part 1
position = "AAA"
step = 0
while position != "ZZZ":
    leftright = instructions[step % len(instructions)]
    position = do_one_step(leftright, position)
    step += 1
print(step)


# part 2
positions = [i for i in list(maps_d.keys()) if i[-1] == "A"]

# find loops
loop = {}
for position in positions:
    step = 0
    step_before = step
    start_position = position
    for i in range(1_000_000):
        leftright = instructions[step % len(instructions)]
        position = do_one_step(leftright, position)
        step += 1
        if position[-1] == "Z":
            loop[start_position] = step - step_before
            step_before = step
        if step > 80_000:  # groot genoeg getal zodat er altijd 1 loop is
            break

# find LCM
lcm = 1
for i in list(loop.values()):
    lcm = lcm * i // gcd(lcm, i)
print(lcm)
