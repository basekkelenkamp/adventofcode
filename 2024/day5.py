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
    print(f"Processing update: {updates.index(update)}")
    poss_orders = []

    for order in orders:
        if all([o in update for o in order]):
            poss_orders.append(order)

    valid = True
    processed_orders = set()
    while True:
        invalid_orders = []

        for poss_order in poss_orders:
            if tuple(poss_order) in processed_orders:
                continue
            if update.index(poss_order[0]) > update.index(poss_order[1]):
                invalid_orders.append(poss_order)
                valid = False

        if not invalid_orders:
            break

        for invalid_order in invalid_orders:
            i1 = update.index(invalid_order[0])
            i2 = update.index(invalid_order[1])
            print(f"Swapping: {update[i1]} with {update[i2]} in {update}")
            update[i1], update[i2] = update[i2], update[i1]
            processed_orders.add(tuple(invalid_order))  # Convert list to tuple

    if not valid:
        middle_index = len(update) // 2
        count += int(update[middle_index])
        print(f"Finished update: {updates.index(update)} with middle value {update[middle_index]}")

#fuck this shit
print(f"Final count: {count}")
