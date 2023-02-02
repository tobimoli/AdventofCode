# %%
import re
import os
import numpy as np

DAY = str(25)

os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")

# hallop

def character_convert(character):
    if character == '2':
        return 2
    elif character == '1':
        return 1
    elif character == '0':
        return 0
    elif character == '-':
        return -1
    elif character == '=':
        return -2
    else:
        print(f'Something is wrong with character: {character}')

def SNAFU2Decimal(snafu):
    length = len(snafu)
    som = 0
    for idx, item in enumerate(snafu):
        som += 5**(length - idx - 1) * character_convert(item)
    return som

def Decimal2SNAFU(decimal):
    snafu, rest = first_snafu(decimal)
    # compute length
    length = length_snafu(decimal)
    for i in reversed(range(length - 1)):
        nr = round(rest / 5**i)
        rest = rest - nr * 5**i
        snafu += get_simple_snafu(nr)
    return snafu

def length_snafu(decimal):
    condition = True
    som = []
    while condition:
        som.append(2 * 5**len(som))
        if decimal <= sum(som):
            condition = False
    return len(som)

def get_simple_snafu(dec):
    if dec == 1:
        return '1'
    elif dec == 2:
        return '2'
    elif dec == 0:
        return '0'
    elif dec == -1:
        return '-'
    elif dec == -2:
        return '='
    else:
        print('smt is wrong with input')

def first_snafu(dec):
    length = length_snafu(dec)

    # maak lijsten
    lst1 = [5**i for i in range(length)]  # [1, 5, 25, 125, ...]
    lst2 = [2 * 5**i for i in range(length)]  # [2, 10, 50, 250, ...]
    lst3 = list(np.cumsum(lst2))
    lst4 = [lst1[i] if i == 0 else lst1[i] + lst3[i - 1] for i in range(length)]

    number_in_kwestie = lst4[-1]

    if dec <= number_in_kwestie:
        return '1', dec - lst1[-1]
    else:
        return '2', dec - lst2[-1]

def convert_to_decimals(data):
    decimals = []
    for snafu in data:
        decimals.append(SNAFU2Decimal(snafu))
    return decimals

def main(data):
    decimals = convert_to_decimals(data)
    som = sum(decimals)
    answer = Decimal2SNAFU(som)
    return answer

# part 1
print(main(TEST))
print(main(DATA))

# %%
