def run_simulation(lines, direction, pos):
    for h, line in enumerate(lines):
        if "^" in line:
            pos = (h, line.index("^"))
            break

    track_pos_and_dir = set()
    while True:
        # ----------------
        if direction == "^":
            if pos[0] == 0:
                raise IndexError("Reached top")

            if lines[pos[0] - 1][pos[1]] == "#":
                direction = ">"
                continue
            else:
                pos = (pos[0] - 1, pos[1])
                if (pos, direction) in track_pos_and_dir:
                    print("Loop detected")
                    break
                else:
                    track_pos_and_dir.add((pos, direction))

        # ----------------
        elif direction == ">":
            if pos[1] == len(lines[0]) - 1:
                raise IndexError("Reached right")

            if lines[pos[0]][pos[1] + 1] == "#":
                direction = "v"
                continue
            else:
                pos = (pos[0], pos[1] + 1)
                if (pos, direction) in track_pos_and_dir:
                    print("Loop detected")
                    break
                else:
                    track_pos_and_dir.add((pos, direction))

        # ----------------
        elif direction == "v":
            if pos[0] == len(lines) - 1:
                raise IndexError("Reached bottom")

            if lines[pos[0] + 1][pos[1]] == "#":
                direction = "<"
                continue
            else:
                pos = (pos[0] + 1, pos[1])
                if (pos, direction) in track_pos_and_dir:
                    print("Loop detected")
                    break
                else:
                    track_pos_and_dir.add((pos, direction))

        # ----------------
        elif direction == "<":
            if pos[1] == 0:
                raise IndexError("Reached left")

            if lines[pos[0]][pos[1] - 1] == "#":
                direction = "^"
                continue
            else:
                pos = (pos[0], pos[1] - 1)
                if (pos, direction) in track_pos_and_dir:
                    print("Loop detected")
                    break
                else:
                    track_pos_and_dir.add((pos, direction))
    return


def main():
    file = open("data/6.txt", "r")
    lines = [line.strip() for line in file.readlines()]
    direction = "^"
    pos = (0, 0)  # (h, w)
    obstruction = (0, 0)
    unique_obstructions = set()
    for h, line in enumerate(lines):
        for w, char in enumerate(line):
            if char == "^" or char == "#":
                continue
            obstruction = (h, w)
            temp_lines = lines.copy()
            temp_lines[h] = temp_lines[h][:w] + "#" + temp_lines[h][w + 1:]

            try:
                run_simulation(temp_lines, direction, pos)
                unique_obstructions.add(obstruction)
            except IndexError:
                print(f"Out of bound, no loop detected. Obstruction at {obstruction}")

    print(f"Unique obstructions: {len(unique_obstructions)}")
    return


if __name__ == "__main__":
    main()


