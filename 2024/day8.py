def check_around(lines, char, h, w):
    directions = [
        (1, 0),  # Down
        (-1, 0),  # Up
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 1),  # Down-Right
        (-1, -1),  # Up-Left
        (1, -1),  # Down-Left
        (-1, 1)  # Up-Right
    ]

    max_depth = max(len(lines), len(lines[0]))
    depth = 1
    while depth <= max_depth:
        for dh, dw in directions:
            nh, nw = h + depth * dh, w + depth * dw
            if 0 <= nh < len(lines) and 0 <= nw < len(lines[0]) and lines[nh][nw] == char:
                return nh, nw
        depth += 1

    return False


def main():
    file = open("data/8.txt", "r")
    lines = [line.strip() for line in file.readlines()]
    anti_nodes = []
    for h, line in enumerate(lines):
        for w, char in enumerate(line):
            if char == ".":
                continue
            print(f"Checking: {char}, pos: {h},{w}")
            pos = check_around(lines, char, h, w)
            if pos:
                print(f"found '{char}': {pos}")


if __name__ == "__main__":
    main()
