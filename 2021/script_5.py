import csv
from pprint import pprint

sorted_list = []
with open('input5.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        r_split = row[1].split()
        _line = {
            "x1": row[0],
            "y1": r_split[0],
            "x2": r_split[2],
            "y2": row[2]
        }
        sorted_list.append(_line)

pprint(sorted_list)


def calculate_line(line: dict):
    # calculate if vertical or horizontal
    if line["x1"] is line["x2"]:
        print(f"vertical: {line}")

    if line["y1"] is line["y2"]:
        print(f"horizontal: {line}")


for line in sorted_list:
    calculate_line(line)


breakpoint()
