f = open("input_day7.txt", "r")
data = f.read().split("\n")
f.close()

# PART 1
J_IS_JOKER = False


def find_unique_characters(cards):
    unique_chars = []
    for i in cards:
        if i not in unique_chars:
            unique_chars.append(i)
    return unique_chars


def find_type(cards: str) -> int:
    unique_chars = find_unique_characters(cards)
    if J_IS_JOKER and ("J" in cards):
        return find_type_with_joker(cards)

    if len(unique_chars) == 1:
        return 7  # five of a kind
    elif len(unique_chars) == 2:
        if any([cards.count(ch) == 4 for ch in unique_chars]):
            return 6  # four of a kind
        else:
            return 5  # full house
    elif len(unique_chars) == 3:
        if any([cards.count(ch) == 3 for ch in unique_chars]):
            return 4  # three of a kind
        else:
            return 3  # two pair
    elif len(unique_chars) == 4:
        return 2  # one pair
    else:
        return 1  # high card


def card1_higher_than_card2(card1, card2) -> bool:
    if J_IS_JOKER:
        replace = {"A": 14, "K": 13, "Q": 12, "T": 10, "J": 0}
    else:
        replace = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    if card1 in replace:
        card1 = replace[card1]
    if card2 in replace:
        card2 = replace[card2]
    return int(card1) > int(card2)


def cards1_higher_than_cards2(cards1: str, cards2: str) -> bool:
    for i in range(5):
        card1 = cards1[i]
        card2 = cards2[i]
        if card1 == card2:
            continue
        return card1_higher_than_card2(card1, card2)
    raise TypeError


def bubbleSort(arr):
    n = len(arr)

    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            # is greater than the adjacent element
            if cards1_higher_than_cards2(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# hand with corresponding bid
bids = {}
for hand in data:
    cards, bid = hand.split()
    bid = int(bid)
    bids[cards] = bid

hands = {i: [] for i in range(1, 8)}
# find rank for each hand
for hand in data:
    cards, _ = hand.split()

    hands[find_type(cards)].append(cards)


# order the hands
order = []
for type_hand, hands_cards in hands.items():
    if len(hands_cards) == 0:
        continue
    elif len(hands_cards) == 1:
        order.append(bids[hands_cards[0]])
    else:
        sorting = bubbleSort(hands_cards)
        bids_in_order = [bids[card] for card in sorting]
        order += bids_in_order

winnings = sum([(rank + 1) * bid for rank, bid in enumerate(order)])
print(winnings)


# part 2
J_IS_JOKER = True


def find_type_with_joker(cards: str) -> int:
    unique_chars = find_unique_characters(cards)
    cards_not_joker = [i for i in unique_chars if i != "J"]

    # vind meest voorkomende kaart
    max_counts = 0
    most_common_card = "J"
    for card_not_joker in cards_not_joker:
        counts = cards.count(card_not_joker)
        if counts > max_counts:
            most_common_card = card_not_joker
            max_counts = counts

    # vervang joker door meest voorkomende kaart
    cards = cards.replace("J", most_common_card)

    unique_chars = find_unique_characters(cards)

    if len(unique_chars) == 1:
        return 7  # five of a kind
    elif len(unique_chars) == 2:
        if any([cards.count(ch) == 4 for ch in unique_chars]):
            return 6  # four of a kind
        else:
            return 5  # full house
    elif len(unique_chars) == 3:
        if any([cards.count(ch) == 3 for ch in unique_chars]):
            return 4  # three of a kind
        else:
            return 3  # two pair
    elif len(unique_chars) == 4:
        return 2  # one pair
    else:
        return 1  # high card


hands = {i: [] for i in range(1, 8)}
# find rank for each hand
for hand in data:
    cards, _ = hand.split()

    hands[find_type(cards)].append(cards)


# order the hands
order = []
for type_hand, hands_cards in hands.items():
    if len(hands_cards) == 0:
        continue
    elif len(hands_cards) == 1:
        order.append(bids[hands_cards[0]])
    else:
        sorting = bubbleSort(hands_cards)
        bids_in_order = [bids[card] for card in sorting]
        order += bids_in_order

winnings = sum([(rank + 1) * bid for rank, bid in enumerate(order)])
print(winnings)
