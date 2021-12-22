import numpy as np
filename = 'input_day4.txt'
numbers = np.loadtxt(filename, delimiter=',', skiprows=0, max_rows = 1, dtype=int)
lines = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=str)

size = len(lines)
cards = np.zeros((size//5, 5, 5))
check_new = np.ones(cards.shape)

for nmr, card in enumerate(cards):
    for ind, line in enumerate(lines[nmr*5 : (nmr+1)*5]):
        card[ind, :] = list(map(int, line.split()))

def bingo(cards, return_card = False):
    bingos = np.zeros(len(cards))
    for card_nr, card in enumerate(cards):
        for row in card:
            if np.sum(row) == 0:
                bingos[card_nr] = 1
        for col in card.T:
            if np.sum(col) == 0:
                bingos[card_nr] = 1
    if return_card:
        return np.argwhere(bingos == 0)[0][0]
    if np.sum(bingos) == len(cards):
        return True
    else:
        return False

def fill_in(cards, number, check):
    check_new = check.copy()
    for i, card in enumerate(cards):
        for j, row in enumerate(card):
            for k, val in enumerate(row):
                if val == number:
                    check_new[i,j,k] = 0
    return check_new


nmr = -1
BINGO = False
while not BINGO:
    nmr += 1
    check_old = check_new
    number = numbers[nmr]
    check_new = fill_in(cards, number, check_old)
    BINGO = bingo(check_new)    

card_nr = bingo(check_old, True)
final_nr = number

answer = final_nr * np.sum(check_new[card_nr] * cards[card_nr])
print(answer)