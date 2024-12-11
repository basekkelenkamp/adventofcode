from itertools import combinations
from collections import defaultdict

def add_tuple(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]

def subtract_tuple(t1, t2):
    return t1[0] - t2[0], t1[1] - t2[1]

def main():
    file = open("data/8.txt", "r")
    lines = [line.strip() for line in file.readlines()]
    char_pos = defaultdict(list)
    board_size = (len(lines) - 1, len(lines[0]) - 1)
    for h, line in enumerate(lines):
        for w, char in enumerate(line):
            if char == ".":
                continue
            char_pos[char].append((h, w))

    anti_nodes = []
    combs = defaultdict(list)
    for char, positions in char_pos.items():
        if len(positions) > 1:
            for comb in combinations(positions, 2):
                combs[char].append(list(comb))

                diff = (comb[1][0] - comb[0][0], comb[1][1] - comb[0][1])
                print(f"{comb} -> diff: {diff}")
                add = add_tuple(comb[0], diff)
                sub = subtract_tuple(comb[1], diff)
                print(f"add: {add}, sub: {sub}")
                if all([add[0] >= 0, add[0] < board_size[0], add[1] >= 0, add[1] < board_size[1]]):
                    anti_nodes.append(add)
                if all([sub[0] >= 0, sub[0] < board_size[0], sub[1] >= 0, sub[1] < board_size[1]]):
                    anti_nodes.append(sub)

    print(len(anti_nodes))
    print(len(set(anti_nodes)))
if __name__ == "__main__":
    main()
