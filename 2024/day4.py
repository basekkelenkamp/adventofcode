file = open("data/4.txt", "r")
lines = [line.strip() for line in file.readlines()]

count = 0
for h, line in enumerate(lines):
    for w, char in enumerate(line):
        if char != "X":
            continue

        # (<--)
        if w >= 3:
            word = line[w-3:w+1]
            if word == "XMAS" or word[::-1] == "XMAS":
                print(f"[{h}:{w}] <-- {word}")
                count += 1

        # (-->)
        if w <= len(line) - 4:
            word = line[w:w+4]
            if word == "XMAS" or word[::-1] == "XMAS":
                print(f"[{h}:{w}] --> {word}")
                count += 1

        # (^)
        if h >= 3:
            word = ''.join([lines[h - i][w] for i in range(0, 4)])
            if word == "XMAS" or word[::-1] == "XMAS":
                print(f"[{h}:{w}] ^ {word}")
                count += 1

        # (v)
        if h <= len(lines) - 4:
            word = ''.join([lines[h + i][w] for i in range(0, 4)])
            if word == "XMAS" or word[::-1] == "XMAS":
                print(f"[{h}:{w}] v {word}")
                count += 1

        # (<^)
        if h >= 3 and w >= 3:
            word = ''.join([lines[h - i][w - i] for i in range(0, 4)])
            if word == "XMAS" or word[::-1] == "XMAS":
                print(f"[{h}:{w}] <^ {word}")
                count += 1

        # (<v)
        if h <= len(lines) - 4 and w >= 3:
            word = ''.join([lines[h + i][w - i] for i in range(0, 4)])
            if word == "XMAS" or word[::-1] == "XMAS":
                print(f"[{h}:{w}] <v {word}")
                count += 1

        # (>^)
        if h >= 3 and w <= len(line) - 4:
            word = ''.join([lines[h - i][w + i] for i in range(0, 4)])
            if word == "XMAS" or word[::-1] == "XMAS":
                print(f"[{h}:{w}] >^ {word}")
                count += 1

        # (>v)
        if h <= len(lines) - 4 and w <= len(line) - 4:
            word = ''.join([lines[h + i][w + i] for i in range(0, 4)])
            if word == "XMAS" or word[::-1] == "XMAS":
                print(f"[{h}:{w}] >v {word}")
                count += 1

print(f"part1: {count}")

# Part 2

count = 0
for h, line in enumerate(lines):
    for w, char in enumerate(line):
        if char != "A" or w <= 0 or w >= len(line) - 1 or h <= 0 or h >= len(lines) - 1:
            continue

        mas1 = ''.join([lines[h - 1][w - 1], char, lines[h + 1][w + 1]])
        mas2 = ''.join([lines[h - 1][w + 1], char, lines[h + 1][w - 1]])
        if mas1 in ["MAS", "SAM"] and mas2 in ["MAS", "SAM"]:
            count += 1
            print(f"[{h}:{w}] {mas1} {mas2}")

print(f"part2: {count}")
