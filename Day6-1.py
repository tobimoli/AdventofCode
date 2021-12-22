import numpy as np
filename = 'input_day6.txt'
fishes = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=int)

#%% very slow method:
DAYS = 80
for day in range(1, DAYS + 1):
    new_fishes = []
    for fish_nr, fish in enumerate(fishes):
        if fish > 0:
            fishes[fish_nr] -= 1
        else:
            fishes[fish_nr] = 6
            new_fishes.append(8)
    fishes = np.append(fishes, new_fishes)

nr_of_fish = len(fishes)
print(nr_of_fish)
#%% very fast method

fishes = list(np.loadtxt(filename, delimiter=',', skiprows=0, dtype=int))

DAYS = 256
current_states = {
    0: fishes.count(0),
    1: fishes.count(1),
    2: fishes.count(2),
    3: fishes.count(3),
    4: fishes.count(4),
    5: fishes.count(5),
    6: fishes.count(6),
    7: fishes.count(7),
    8: fishes.count(8)
}
next_states = {}
for day in range(1, DAYS + 1):
    next_states = {
        0: current_states[1],
        1: current_states[2],
        2: current_states[3],
        3: current_states[4],
        4: current_states[5],
        5: current_states[6],
        6: current_states[7],
        7: current_states[8],
        8: current_states[0]
    }

    next_states[6] += current_states[0]
    current_states = next_states
    next_states = {}
total = 0
for fish in current_states:
    total += current_states[fish]
print(total)
