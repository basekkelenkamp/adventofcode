import csv

list_data = []
with open('3.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        list_data.append(row[0])

print(list_data)

gamma_rate = ''
epsilon_rate = ''

element_length = 0
count_zero = 0
count_one = 0

list_of_counts = {}
for index, digit in enumerate(list_data[0]):
    list_of_counts[str(index)] = {
        "one": 0,
        "zero": 0
    }


for binary_number in list_data:

    for index, element in enumerate(binary_number):
        element_length = element_length + 1
        i = str(index)
        if "0" in element:
            list_of_counts[i]["zero"] = list_of_counts[i]["zero"] + 1

        if "1" in element:
            list_of_counts[i]["one"] = list_of_counts[i]["one"] + 1


for index in list_of_counts:
    if list_of_counts[index]["zero"] < list_of_counts[index]["one"]:
        gamma_rate = gamma_rate + "1"
    else:
        gamma_rate = gamma_rate + "0"

print(gamma_rate)

for digit in str(gamma_rate):
    if digit == "0":
        epsilon_rate = epsilon_rate + "1"
    else:
        epsilon_rate = epsilon_rate + "0"

print(epsilon_rate)

print(f"gamma: {int(gamma_rate, 2)}, epsilon: {int(epsilon_rate, 2)}. Total:{int(gamma_rate, 2) * int(epsilon_rate, 2)}")
breakpoint()
