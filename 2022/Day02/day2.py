# %%
import os

import numpy as np

with open("input_day2.txt", "r") as f:
    data = f.read().split("\n")


def rock_paper_scissors(player1, player2):
    points = 0
    if player2 == "X":
        points += 1
        if player1 == "C":
            points += 6
        elif player1 == "A":
            points += 3
    elif player2 == "Y":
        points += 2
        if player1 == "A":
            points += 6
        elif player1 == "B":
            points += 3
    elif player2 == "Z":
        points += 3
        if player1 == "B":
            points += 6
        elif player1 == "C":
            points += 3
    return points


def lose_draw_win(player1, outcome):
    if player1 == "A":  # rock
        if outcome == "X":
            player2 = "Z"
        elif outcome == "Y":
            player2 = "X"
        else:
            player2 = "Y"
    elif player1 == "B":  # paper
        if outcome == "X":
            player2 = "X"
        elif outcome == "Y":
            player2 = "Y"
        else:
            player2 = "Z"
    else:  # scissors
        if outcome == "X":
            player2 = "Y"
        elif outcome == "Y":
            player2 = "Z"
        else:
            player2 = "X"
    return player2


# part 1
points_game = 0
for round in data:
    opponent_choice = round[0]
    your_choice = round[-1]

    points_game += rock_paper_scissors(opponent_choice, your_choice)

print(points_game)

# part 2
points_game = 0
for round in data:
    opponent_choice = round[0]
    losedrawwin = round[-1]

    your_choice = lose_draw_win(opponent_choice, losedrawwin)

    points_game += rock_paper_scissors(opponent_choice, your_choice)

print(points_game)

# %%
