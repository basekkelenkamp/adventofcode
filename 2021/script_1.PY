import csv

list_data = []
with open('tmp2.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        list_data.append(int(row[0]))

count = 0
window_count = 0
previous = 10000000
index = 0
list_length = len(list_data)
summed = 0

window_measurements = []

for item in list_data:
    for measurement in list_data[len(window_measurements):]:
        if window_count == 3:
            window_measurements.append(summed)
            window_count = 0
            summed = 0
            break

        summed = summed + measurement
        window_count = window_count + 1

for item in window_measurements:
    if previous < item:
        count = count + 1
    previous = item

print(window_measurements)
print(f"result:{count}")
