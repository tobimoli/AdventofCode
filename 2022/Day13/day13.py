# %%
import json
import os
import string

DAY = str(13)

# os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")


def get_pair(data, pair):
    pair_left = json.loads(data[pair * 3])
    pair_right = json.loads(data[pair * 3 + 1])
    return pair_left, pair_right


def compare(pair_left, pair_right):
    if isinstance(pair_left, int) and isinstance(pair_right, int):
        if pair_left < pair_right:
            return -1
        elif pair_left > pair_right:
            return +1
        else:
            return 0
    elif isinstance(pair_left, int):
        pair_left = [pair_left]
    elif isinstance(pair_right, int):
        pair_right = [pair_right]

    if pair_left == [] and pair_right != []:
        return -1
    elif pair_left != [] and pair_right == []:
        return +1
    elif pair_left == [] and pair_right == []:
        return 0
    tf = compare(pair_left[0], pair_right[0])
    if tf:
        return tf
    else:
        return compare(pair_left[1:], pair_right[1:])


def read(data):
    lst = []
    for line in data:
        if line != "":
            lst.append(json.loads(line))
    return lst


def main(data):
    answer = 0
    size = len(data)
    n_pairs = (size + 1) // 3
    for pair in range(n_pairs):
        p_left, p_right = get_pair(data, pair)
        if compare(p_left, p_right) == -1:
            answer += pair + 1
    return answer


def main2(data):
    extra_packets = [[[2]], [[6]]]
    data = read(data)
    for i in extra_packets:
        data.append(i)

    sorted_lst = []
    while len(data) > 0:
        sommen = [0] * len(data)
        for i, item_i in enumerate(data):
            for j, item_j in enumerate(data[i + 1 :]):
                if compare(item_i, item_j) == -1:
                    sommen[i] += 1
                else:
                    sommen[i + j + 1] += 1
        idx = sommen.index(max(sommen))
        sorted_lst.append(data[idx])
        del data[idx]

    factor = 1
    for i in extra_packets:
        idx = sorted_lst.index(i)
        factor *= idx + 1
    return factor


# part 1
print(main(TEST))
print(main(DATA))

# part 2
print(main2(TEST))
print(main2(DATA))

# %%
