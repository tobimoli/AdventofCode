import numpy as np
filename = 'input_day4.txt'
numbers = np.loadtxt(filename, delimiter=',', skiprows=0, max_rows = 1, dtype=int)
lines = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=str)

size = len(lines)
cards = np.zeros((size//5, 5, 5))
check = np.ones(cards.shape)

for nmr, card in enumerate(cards):
    for ind, line in enumerate(lines[nmr*5 : (nmr+1)*5]):
        card[ind, :] = list(map(int, line.split()))

def bingo(cards, return_card = False):
    for card_nr, card in enumerate(cards):
        for row in card:
            if np.sum(row) == 0:
                if return_card:
                    return card_nr
                else:
                    return True
        for col in card.T:
            if np.sum(col) == 0:
                if return_card:
                    return card_nr
                else:
                    return True
    return False

def fill_in(cards, number, check):
    for i, card in enumerate(cards):
        for j, row in enumerate(card):
            for k, val in enumerate(row):
                if val == number:
                    check[i,j,k] = 0
    return check


nmr = -1
BINGO = False
while not BINGO:
    nmr += 1
    number = numbers[nmr]
    check = fill_in(cards, number, check)
    BINGO = bingo(check)
    

card_nr = bingo(check, True)
final_nr = number

answer = final_nr * np.sum(check[card_nr] * cards[card_nr])
print(answer)