import csv
from pprint import pprint

list_data = []
with open('3.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        list_data.append(row[0])

print(list_data)

gamma_rate = ''
epsilon_rate = ''

list_of_counts = {}
for index, digit in enumerate(list_data[0]):
    list_of_counts[str(index)] = {
        "one": 0,
        "zero": 0
    }

binarys_to_remove1 = []
oxygen_rating = list_data

for binary_number in oxygen_rating:

    for index, element in enumerate(binary_number):
        row_list = [[item for sublist in x for item in sublist] for x in zip(*oxygen_rating)]
        if len(row_list[0]) == 1:
            break

        for delete_binary in binarys_to_remove1:
            oxygen_rating.remove(delete_binary)

        i = str(index)
        print(row_list)
        binarys_to_remove1 = []

        if row_list[index].count("1") > row_list[index].count("0") or row_list[index].count("1") == row_list[index].count("0"):
            for binary in oxygen_rating:
                if binary[int(i)] == "0":
                    pprint(f"REMOVED: {binary}")
                    binarys_to_remove1.append(binary)

        if row_list[index].count("1") < row_list[index].count("0"):
            for binary in oxygen_rating:
                if binary[int(i)] == "1":
                    binarys_to_remove1.append(binary)
                    pprint(f"REMOVED: {binary}")

print("\n\n\n\n")

binarys_to_remove = []
scrubber_rating = []
with open('3.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        scrubber_rating.append(row[0])

for binary_number in scrubber_rating:

    for index, element in enumerate(binary_number):

        row_list = [[item for sublist in x for item in sublist] for x in zip(*scrubber_rating)]
        if len(row_list[0]) == 1:
            break

        for delete_binary in binarys_to_remove:
            scrubber_rating.remove(delete_binary)

        i = str(index)
        pprint(row_list)
        pprint(scrubber_rating)
        print(f"loop count: {i}")
        binarys_to_remove = []

        if row_list[index].count("1") > row_list[index].count("0") or row_list[index].count("1") == row_list[index].count("0"):
            for binary in scrubber_rating:
                print(f"removing all numbers with index: {index}, 0 is least common. Current value: {binary}")
                if binary[index] == "1":
                    binarys_to_remove.append(binary)
                    pprint(f"REMOVED: {binary}")

        elif row_list[index].count("1") < row_list[index].count("0"):
            for binary in scrubber_rating:
                print(f"removing all numbers with index: {index}, 1 is least common. Current value: {binary}")
                if binary[index] == "0":
                    binarys_to_remove.append(binary)
                    pprint(f"REMOVED: {binary}")


print("\n\n\n\n")
print(f"oxygen rating is: {oxygen_rating}")
print(f"scrubber rating is: {scrubber_rating}")


print(f"oxygen: {int(oxygen_rating[0], 2)}, epsilon: {int(scrubber_rating[0], 2)}. Total:{int(oxygen_rating[0], 2) * int(scrubber_rating[0], 2)}")
breakpoint()
