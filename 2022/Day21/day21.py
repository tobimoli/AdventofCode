# %%

DAY = str(21)

# os.chdir(f"/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day{DAY}")
with open(f"input_day{DAY}.txt", "r") as f:
    DATA = f.read().split("\n")
with open(f"test_day{DAY}.txt", "r") as f:
    TEST = f.read().split("\n")


def read_data(data):
    dic = {}
    for line in data:
        name, rest = line.split(": ")
        if rest.isnumeric():
            rest = int(rest)
        else:
            rest = [rest[:4], rest[5], rest[7:]]
        dic[name] = rest
    return dic


def update_monkey(dic, monkey):
    # print(f"Updating monkey: {monkey}")
    job = dic[monkey]
    value1 = dic[job[0]]
    value2 = dic[job[2]]
    operator = job[1]
    if operator == "+":
        new_value = value1 + value2
    elif operator == "-":
        new_value = value1 - value2
    elif operator == "*":
        new_value = value1 * value2
    else:
        new_value = value1 / value2
    dic[monkey] = int(new_value)
    return dic


def monkey_can_yell_number(dic, job):
    value1 = dic[job[0]]
    value2 = dic[job[2]]

    if isinstance(value1, int) and isinstance(value2, int):
        return True
    return False


def update_monkeys(dic):
    job_root = dic["root"]
    while not monkey_can_yell_number(dic, job_root):
        for monkey, job in dic.items():
            if monkey != "root":
                if isinstance(job, list) and monkey_can_yell_number(dic, job):
                    dic = update_monkey(dic, monkey)
                    job_root = dic["root"]
    return dic


def equal(dic, monkey):
    job = dic[monkey]
    value1 = dic[job[0]]
    value2 = dic[job[2]]
    return value1 == value2


def main(data):
    dic = read_data(data)
    dic = update_monkeys(dic)
    dic = update_monkey(dic, "root")
    return dic["root"]


def main2(data):
    for yell in range(3_006_709_232_000, 3_006_709_233_000, 1):
        dic = read_data(data)
        dic["humn"] = yell
        dic = update_monkeys(dic)
        if equal(dic, "root"):
            return yell
    return "No equality found"


# part 1
print(main(TEST))
print(main(DATA))

# part 2
print(main2(TEST))
# trial and error
print(main2(DATA))
# %%
