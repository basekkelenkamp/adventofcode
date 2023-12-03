file = open("data/day3.txt", "r")
lines = file.readlines()

import regex as re

# part 1
def check_if_symbol_around_number(line: str, start: int, end: int):
    symbols = '+&/@=-$*#%'

    if start == 0:
        start = 1

    try:
        sub_line = line[start-1:end+1]
    except IndexError:
        sub_line = line[start-1:end]

    for symbol in symbols:
        if symbol in sub_line:
            return True
    else:
        return False
    

valid_numbers = []
for index, line_current in enumerate(lines):
    line_current = line_current.strip()
    line_prev = lines[index - 1].strip()

    if index == 0:
        line_prev = False
    
    if index == len(lines) - 1:
        line_next = False
    else:
        line_next = lines[index + 1].strip()


    # [(number, start, end)]
    numbers_pos = [(m.group(), m.start(), m.end()) for m in re.finditer(r"\d+", line_current)]

    for _number in numbers_pos:
        number = _number[0]
        start = _number[1]
        end = _number[2]

        print(number)

        if check_if_symbol_around_number(line_current, start, end):
            print("found", number, "because of", "line_current")
            valid_numbers.append(int(number))

        if line_next:
            if check_if_symbol_around_number(line_next, start, end):
                print("found", number, "because of", "line_next")
                valid_numbers.append(int(number))
        if line_prev:
            if check_if_symbol_around_number(line_prev, start, end):
                print("found", number, "because of", "line_prev")
                valid_numbers.append(int(number))


print("part 1:", sum(valid_numbers))


# part 2
def return_number_around_gear(line: str, gear_pos: int):
    
    # [(number, start, end)]
    numbers_pos = [(m.group(), m.start(), m.end()) for m in re.finditer(r"\d+", line)]
    gear_range = range(max(0, gear_pos-1), min(len(line) - 1, gear_pos+2))

    numbers = []
    for _number in numbers_pos:
        number = _number[0]
        start = _number[1]
        end = _number[2]
        num_range = range(start, end)

        print("gear range:", gear_range)
        print("num range:", num_range)

        g = set(gear_range)
        overlap = g.intersection(num_range)
        if len(overlap) > 0:
            numbers.append(int(number))

    return numbers



gear_sum = 0
for index, line_current in enumerate(lines):
    line_current = line_current.strip()
    line_prev = lines[index - 1].strip()

    if index == 0:
        line_prev = False
    
    if index == len(lines) - 1:
        line_next = False
    else:
        line_next = lines[index + 1].strip()


    # [(number, start, end)]
    gears = [m.start() for m in re.finditer(r"\*", line_current)]
    for gear_pos in gears:
        gear_numbers = []

        print(gear_pos)

        curr = return_number_around_gear(line_current, gear_pos)
        if curr:
            gear_numbers.extend(curr)
            print("found numbers:", curr, "because of", "line_current")

        if line_next:
            nex = return_number_around_gear(line_next, gear_pos)
            if nex:
                print("found numbers:", nex, "because of", "line_next")
                gear_numbers.extend(nex)

        if line_prev:
            prev = return_number_around_gear(line_prev, gear_pos)
            if prev:
                print("found numbers:", gear_pos, "because of", "line_prev")
                gear_numbers.extend(prev)

        print(gear_numbers)
        if len(gear_numbers) == 2:
            gear_sum += gear_numbers[0] * gear_numbers[1]

print("part 2:", gear_sum)

