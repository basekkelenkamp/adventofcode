file = open("data/day4.txt", "r")
lines = file.readlines()
from pprint import pprint as pp

def create_list_of_nums(num_string: str):
    nums = []
    for num in num_string.split(" "):
        if not num == "":
            nums.append(int(num))
    return nums

# part 1
total = 0
for line in lines:
    line = line.strip()
    line = line.split(": ")[1]
    winning, input = line.split("|")

    winning = create_list_of_nums(winning)
    input = create_list_of_nums(input)

    count = 0
    for num in input:
        if num in winning:
            count += 1
    
    if count > 0:
        points = 1
        for _ in range(count-1):
            points *= 2
        total += points

print(f"Points: {total} (Part 1)")


# part 2
total_cards = 0
score_per_line = { f"card: {i}":{"copies": 1} for i, line in enumerate(lines, start=1) }
for card_index, line in enumerate(lines, start=1):
    print(f"Card {card_index}")
    total_cards += 1

    line = line.strip()
    line = line.split(": ")[1]
    winning, input = line.split("|")

    winning = create_list_of_nums(winning)
    input = create_list_of_nums(input)

    winning_count = 0
    for num in input:
        if num in winning:
            winning_count += 1
    
    if winning_count > 0:
        for _ in range(score_per_line[f"card: {card_index}"]["copies"]):
            _range = range(card_index+1, card_index + winning_count + 1)
            for i in _range:
                score_per_line[f"card: {i}"]["copies"] += 1
    

total_copies = sum(card['copies'] for card in score_per_line.values())
print(f"Total scratchcards (part 2):")
pp(total_copies)
