import os

os.chdir(r"Y:\Fun\AdventofCode\AdventofCode\2023\Day01")

f = open("input_day1.txt", "r")
data = f.read().split("\n")
f.close()

# part 1
answer = 0
for row in data:
    row_digits = [int(d) for d in row if d.isdigit()]

    first_number = row_digits[0]
    last_number = row_digits[-1]

    number = first_number * 10 + last_number
    answer += number

print(answer)

# part 2
number_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
number_digits = {key: f"{key}{num}{key}" for key, num in number_digits.items()}

answer = 0
for row in data:
    for num, dig in number_digits.items():
        row = row.replace(num, number_digits[num])

    row_digits = [int(d) for d in row if d.isdigit()]

    first_number = row_digits[0]
    last_number = row_digits[-1]

    number = first_number * 10 + last_number
    answer += number

print(answer)
