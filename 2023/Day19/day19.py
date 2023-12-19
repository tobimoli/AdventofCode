import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n\n")
f.close()

workflows = data[0].split("\n")
ratings = data[1].split("\n")

# make dictionaries
workflow_d = {}
for w in workflows:
    key, instructions = w.split("{")

    instructions = instructions[:-1]
    instructions = instructions.split(",")

    values = {}
    for nr, i in enumerate(instructions):
        if ":" in i:
            rule, ans = i.split(":")
        else:
            rule, ans = "else", i
        values[nr] = (rule, ans)
    workflow_d[key] = values

ratings_d = []
for r in ratings:
    d = {}
    r = r[1:-1]
    r = r.split(",")
    for i in r:
        key, val = i.split("=")
        d[key] = int(val)
    ratings_d.append(d)


# loop over all items and add to accepted if A
def rule_matched(rule, item) -> bool:
    if rule == "else":
        return True
    i = rule[0]
    diff = rule[1]
    num = int(rule[2:])
    if diff == ">":
        return item[i] > num
    else:
        return item[i] < num


def find_score_bf(ratings_d, workflow_d):
    score = 0

    for item in ratings_d:
        key = "in"
        while key not in ["R", "A"]:
            work = workflow_d[key]

            not_matched = True
            i = 0
            while not_matched:
                rule, ans = work[i]
                if rule_matched(rule, item):
                    new_key = ans
                    not_matched = False
                i += 1
            key = new_key

        if key == "A":
            score += sum(item.values())
    return score


# part 1
print(find_score_bf(ratings_d, workflow_d))

# part 2
# loop door workflow en onthou de condities waarvoor je A terug krijgt

# alle paden bewandelen:


def loop_through_dic(dictionary, key, conditions):
    if key == "A":
        return [conditions]
    elif key == "R":
        return []

    accepted_if = []

    for i, work in dictionary[key].items():
        condition, new_key = work
        if i > 0:
            for j in range(i):
                not_condition, _ = dictionary[key][j]
                if "<" in not_condition:
                    not_condition = not_condition.replace("<", ">=")
                else:
                    not_condition = not_condition.replace(">", "<=")
                conditions += [not_condition]
        new_conditions = conditions
        if condition != "else":
            new_conditions = conditions + [condition]
        accepted_if += loop_through_dic(dictionary, new_key, new_conditions)
    return accepted_if


all_conditions = loop_through_dic(workflow_d, key="in", conditions=[])
som = 0

for condition in all_conditions:
    condition = list(set(condition))

    # condities bij elkaar nemen
    letters = ["x", "m", "a", "s"]
    # waar moet x aan voldoen?
    # x kan 1...4000 zijn
    prod = 1
    for letter in letters:
        range_letter = np.array(list(range(1, 4000 + 1)))
        for cond in condition:
            if cond[2] == "=":
                key, diff, num = cond[0], cond[1:3], cond[3:]
            else:
                key, diff, num = cond[0], cond[1], cond[2:]
            num = int(num)
            if key == letter:
                if diff == ">":
                    range_letter = range_letter[range_letter > num]
                elif diff == ">=":
                    range_letter = range_letter[range_letter >= num]
                elif diff == "<":
                    range_letter = range_letter[range_letter < num]
                else:
                    range_letter = range_letter[range_letter <= num]
        prod *= len(range_letter)
    som += prod
print(som)
