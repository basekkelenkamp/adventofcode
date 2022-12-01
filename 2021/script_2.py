import csv

list_data = []
with open('2.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        list_data.append(row[0])

print(list_data)

horizontal = 0
depth = 0
aim = 0

for item in list_data:
    result = [int(s) for s in item.split() if s.isdigit()]
    print(result)

    if "forward" in item:
        horizontal = horizontal + result[0]
        depth = depth + (aim * result[0])

    elif "down" in item:
        aim = aim + result[0]

    elif "up" in item:
        aim = aim - result[0]

print(f"horizontal: {horizontal}, depth: {depth}. Result: {horizontal * depth}")
