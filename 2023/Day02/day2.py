f = open("input_day2.txt", "r")
data = f.read().split("\n")
f.close()

# part 1
bag = {"red": 12, "green": 13, "blue": 14}

sum_ids = 0
for row in data:
    id = int(row.split(": ")[0].split(" ")[1])
    sets_of_balls = row.split(": ")[1].split("; ")
    max_balls = {"red": 0, "green": 0, "blue": 0}
    for set_of_balls in sets_of_balls:
        colors_amounts = set_of_balls.split(", ")
        for color_amount in colors_amounts:
            amount, color = color_amount.split(" ")
            if int(amount) > max_balls[color]:
                max_balls[color] = int(amount)
    is_possible = True
    for color, max_amount in max_balls.items():
        if max_amount > bag[color]:
            is_possible = False
    if is_possible:
        sum_ids += id

print(sum_ids)

# part 2
sum_powers = 0
for row in data:
    sets_of_balls = row.split(": ")[1].split("; ")
    max_balls = {"red": 0, "green": 0, "blue": 0}
    for set_of_balls in sets_of_balls:
        colors_amounts = set_of_balls.split(", ")
        for color_amount in colors_amounts:
            amount, color = color_amount.split(" ")
            if int(amount) > max_balls[color]:
                max_balls[color] = int(amount)
    power = 1
    for _, amount in max_balls.items():
        power *= amount
    sum_powers += power

print(sum_powers)
