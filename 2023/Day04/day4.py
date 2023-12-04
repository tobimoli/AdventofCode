f = open("input_day4.txt", "r")
data = f.read().split("\n")
f.close()


# part 1
sum_points = 0

for card in data:
    numbers = card.split(": ")[1]
    winning_numbers, numbers_we_have = numbers.split(" | ")

    winning_numbers = winning_numbers.split(" ")
    numbers_we_have = numbers_we_have.split(" ")

    winning_numbers = [int(num) for num in winning_numbers if num != ""]
    numbers_we_have = [int(num) for num in numbers_we_have if num != ""]

    winners = [num for num in numbers_we_have if num in winning_numbers]
    n_winners = len(winners)

    if n_winners == 0:
        continue
    points = 2 ** (n_winners - 1)
    sum_points += points

print(sum_points)

# part 2
cards = {i: 1 for i in range(len(data))}

for i, card in enumerate(data):
    numbers = card.split(": ")[1]
    winning_numbers, numbers_we_have = numbers.split(" | ")

    winning_numbers = winning_numbers.split(" ")
    numbers_we_have = numbers_we_have.split(" ")

    winning_numbers = [int(num) for num in winning_numbers if num != ""]
    numbers_we_have = [int(num) for num in numbers_we_have if num != ""]

    winners = [num for num in numbers_we_have if num in winning_numbers]
    n_winners = len(winners)

    if n_winners == 0:
        continue
    for winner in range(n_winners):
        cards[i + winner + 1] += cards[i]

print(cards)
print(sum(cards.values()))
