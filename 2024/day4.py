file = open("4.txt", "r")
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

print(count)
