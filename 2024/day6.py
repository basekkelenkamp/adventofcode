file = open("data/6.txt", "r")
lines = [line.strip() for line in file.readlines()]

direction = "^"
pos = (0, 0)  # (h, w)
unique_positions = set()

for h, line in enumerate(lines):
    if "^" in line:
        pos = (h, line.index("^"))
        unique_positions.add(pos)
        break

while True:
    try:
        # ----------------
        if direction == "^":
            if pos[0] == 0:
                raise IndexError("Reached top")

            if lines[pos[0] - 1][pos[1]] == "#":
                direction = ">"
                continue
            else:
                pos = (pos[0] - 1, pos[1])
                unique_positions.add(pos)

        # ----------------
        elif direction == ">":
            if pos[1] == len(lines[0]) - 1:
                raise IndexError("Reached right")

            if lines[pos[0]][pos[1] + 1] == "#":
                direction = "v"
                continue
            else:
                pos = (pos[0], pos[1] + 1)
                unique_positions.add(pos)

        # ----------------
        elif direction == "v":
            if pos[0] == len(lines) - 1:
                raise IndexError("Reached bottom")

            if lines[pos[0] + 1][pos[1]] == "#":
                direction = "<"
                continue
            else:
                pos = (pos[0] + 1, pos[1])
                unique_positions.add(pos)

        # ----------------
        elif direction == "<":
            if pos[1] == 0:
                raise IndexError("Reached left")

            if lines[pos[0]][pos[1] - 1] == "#":
                direction = "^"
                continue
            else:
                pos = (pos[0], pos[1] - 1)
                unique_positions.add(pos)

    except IndexError as e:
        print(f"Out of bounds: {e}")
        print(f"Unique positions: {len(unique_positions)}")
        break
