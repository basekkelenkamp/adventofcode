file = open("data/5.txt", "r")

lines = file.readlines()

orders = []
updates = []
for line in lines:
    if "|" in line:
        orders.append(line.strip().split("|"))
    elif "," in line:
        updates.append(line.strip().split(","))

count = 0
for update in updates:
    poss_orders = []
    for order in orders:
        if all(o in update for o in order):
            poss_orders.append(order)

    valid = True
    for poss_order in poss_orders:
        if update.index(poss_order[0]) > update.index(poss_order[1]):
            valid = False
            break

    if valid:
        count += int(update[int((len(update))/2)])
    if not valid:


print(count)
