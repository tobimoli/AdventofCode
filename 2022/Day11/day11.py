# %%
import os

DAY = str(11)

os.chdir(f'/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}')
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")

def read(data):
    info = {}
    for line in data:
        line = line.strip()
        if line == '':
            pass
        elif line[0] == 'M':
            monkey_nr = int(line.split(' ')[1][:-1])
        elif line[0] == 'S':
            items = [int(i) for i in line.split('Starting items: ')[1].split(', ')]
            info[monkey_nr] = {'items': items}
        elif line[0] == 'O':
            operation, value = line.split(' = old ')[1].split(' ')
            info[monkey_nr]['operation'] = [operation, value]
        elif line[0] == 'T':
            test = int(line.split(' ')[-1])
            info[monkey_nr]['test'] = test
        elif line[0] == 'I':
            to_monkey = int(line.split(' ')[-1])
            if 'true' in line:
                info[monkey_nr]['throw_if_true'] = to_monkey
            else:
                info[monkey_nr]['throw_if_false'] = to_monkey
    return info


def apply_operation(item, operation, value):
    if value == 'old':
        value = item
    if operation == '*':
        return item * int(value)
    elif operation == '+':
        return item + int(value)


def do_one_round(dic, lst):
    for monkey, value in dic.items():
        for item in value['items']:
            lst[monkey] += 1
            worry_value = apply_operation(item, value['operation'][0], value['operation'][1])
            worry_value //= 3
            if worry_value % value['test'] == 0:
                dic[value['throw_if_true']]['items'].append(worry_value)
            else:
                dic[value['throw_if_false']]['items'].append(worry_value)
        dic[monkey]['items'] = []
    return dic, lst


def do_one_round_counting(dic, lst):
    modulo = divisible_by(dic)
    for monkey, value in dic.items():
        for item in value['items']:
            lst[monkey] += 1
            worry_value = apply_operation(item, value['operation'][0], value['operation'][1])
            worry_value %= modulo
            if worry_value % value['test'] == 0:
                dic[value['throw_if_true']]['items'].append(worry_value)
            else:
                dic[value['throw_if_false']]['items'].append(worry_value)
        dic[monkey]['items'] = []
    return dic, lst


def compute_answer(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[-1] * sorted_lst[-2]


def divisible_by(dic):
    mult = 1
    for _, value in dic.items():
        mult *= value['test']
    return mult

def main(data, func):
    dic = read(data)
    inspected_items = [0] * len(dic)

    for round in range(ROUNDS):
        dic, inspected_items = func(dic, inspected_items)
        if round + 1 in [1, 20, 1000]:
            print(round, inspected_items)
    return compute_answer(inspected_items)

ROUNDS = 20
print(main(TEST, do_one_round))
print(main(DATA, do_one_round))

ROUNDS = 10000
print(main(TEST, do_one_round_counting))
print(main(DATA, do_one_round_counting))
