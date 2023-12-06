f = open("input_day5.txt", "r")
data = f.read().split("\n")
f.close()


# part 1
seeds = [int(i) for i in data[0].split(": ")[1].split(" ")]


def find_lowest_location(seeds: list):
    # create maps
    maps = {}
    key = ""

    # group lists to each map
    for row in data[2:]:
        if row == "":
            continue
        elif "map" in row:
            key = row
            maps[key] = []
            continue
        maps[key].append([int(i) for i in row.split()])

    locations = []
    for seed in seeds:
        print("SEED")
        next_value = seed

        for mapper, mappings in maps.items():
            print(mapper, next_value)
            found_in_mappings = False
            for mapping in mappings:
                start_d, start_s, length = mapping
                if not found_in_mappings:
                    if (next_value >= start_s) and (next_value < start_s + length):
                        found_in_mappings = True
                        difference = next_value - start_s
                        next_value = start_d + difference

        locations.append(next_value)

    return min(locations)


print(find_lowest_location(seeds))


# part 2
import numpy as np

seeds_row = [int(i) for i in data[0].split(": ")[1].split(" ")]
seeds_couples = np.array(seeds_row).reshape(len(seeds_row) // 2, 2)

seeds = []
for couple in seeds_couples:
    seeds.append(list(range(couple[0], couple[0] + couple[1])))
