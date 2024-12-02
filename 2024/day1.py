file = open("data/1.txt", "r")
lines = file.readlines()

list1 = []
list2 = []
for line in lines:
    a, b = line.split("   ")
    list1.append(a)
    list2.append(b.strip())


list1.sort()
list2.sort()

differences = [abs(int(l1) - int(l2)) for l1, l2 in zip(list1, list2)]
print(sum(differences))

# Part 2

total = 0
for num in list1:
    occurrences = list2.count(num)
    if occurrences != 0:
        total += (int(num) * occurrences)

print(total)