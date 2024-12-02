from pprint import pprint as pp
file = open("data/day7.txt", "r")
lines = file.readlines()
from collections import OrderedDict

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

hand_type = [
    'high card', 
    'one pair', 
    'two pair', 
    'three of a kind', 
    'full house', 
    'four of a kind', 
    'five of a kind'
    ]

labeled_hands = {label: [] for label in hand_type}
labeled_hands = OrderedDict(sorted(labeled_hands.items(), key=lambda t: hand_type[0]))

def calculate_card(card):
    return cards.index(card) + 1

def calculate_hands_from_label(hands_bids):
    hands = [hand.split(' ')[0] for hand in hands_bids]
    bids = [hand.split(' ')[1] for hand in hands_bids]

    calculated_hands_bids = []
    for i, hand in enumerate(hands):
        calculated_hand = []
        for card in hand:
            calculated_hand.append(calculate_card(card))
        
        calculated_hands_bids.append((calculated_hand, bids[i]))
    
    sorted_data = sorted(calculated_hands_bids, key=lambda x: x[0])
    sorted_bids = [bid for _, bid in sorted_data]

    for hand, bid in sorted_data:
        print(hand, bid)
    return sorted_bids



def calculate_hand_type(hand):
    unique_cards = len(set(hand))

    if unique_cards == 1:
        return hand_type[6]
    
    if unique_cards == 2:
        if hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
            return hand_type[5]
        else:
            return hand_type[4]

    if unique_cards == 4:
        return hand_type[1]
    
    if unique_cards == 5:
        return hand_type[0]

    char_count = sorted([hand.count(char) for char in set(hand)], reverse=True)
    if char_count[0] == 3:
        return hand_type[3]
        
    if char_count[0] == 2 and char_count[1] == 2:
        return hand_type[2]


for line in lines:
    line = line.strip()
    hand = line.split(' ')[0]
    labeled_hands[calculate_hand_type(hand)].append(line)


rank = 0
total = 0
for label, hands_bids in labeled_hands.items():
    print(label)

    sorted_bids = calculate_hands_from_label(hands_bids)

    for bid in sorted_bids:
        rank += 1
        total += (rank * int(bid))

        # pp(f"rank: {rank}, bid: {bid}")


print(total)

