file = open("data/day1.txt", "r")
lines = file.readlines()

import regex as re


def insert_into_string(string, substring, index):
    return string[:index] + substring + string[index:]


numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
total = 0

# Part 1
for line in lines:
    for char in line:
        if char in numbers:
            first = char
            for char2 in reversed(line):
                if char2 in numbers:
                    second = char2
                    digit = int(first + second)
                    total += digit
                    break
            break

print("part1: ", total)


# Part 2
numbers_str = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
total = 0

for line in lines:
    # key is index, value is number
    line_object = {}

    for index, char in enumerate(line):
        if char in numbers:
            line_object[index] = char

    for index, str_num in enumerate(numbers_str):
        for m in re.finditer(str_num, line, overlapped=True):
            num_i = m.start()
            if num_i != -1:
                line_object[num_i] = str(index)

    sorted_line_object = dict(sorted(line_object.items()))
    # print(sorted_line_object)

    list_vals = list(sorted_line_object.keys())

    if len(list_vals) == 1:
        total += int(sorted_line_object[list_vals[0]])
        # print("single: ", sorted_line_object[list_vals[0]])
    else:
        # print("total: ", int(sorted_line_object[list_vals[0]] + sorted_line_object[list_vals[-1]]))
        total += int(
            sorted_line_object[list_vals[0]] + sorted_line_object[list_vals[-1]]
        )


print("part2: ", total)


total = 0

for line in lines:
    line = (
        line.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
    )

    numbers = re.findall(rf"\d", line)
    first_number = numbers[0]
    last_number = numbers[-1]

    total += int(first_number + last_number)

print("part2 version2: ", total)
