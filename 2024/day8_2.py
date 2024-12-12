from itertools import combinations
from collections import defaultdict

def get_all_valid_tuples(t1, diff, board_size, op="+"):
    valid_tuples = []
    current = t1
    while True:
        if op == "+":
            current = add_tuple(current, diff)
        else:
            current = subtract_tuple(current, diff)
        if 0 <= current[0] < board_size[0] and 0 <= current[1] < board_size[1]:
            valid_tuples.append(current)
        else:
            break
    return valid_tuples

def add_tuple(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]

def subtract_tuple(t1, t2):
    return t1[0] - t2[0], t1[1] - t2[1]

def main():
    with open("data/8.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]
    char_pos = defaultdict(list)
    board_size = (len(lines), len(lines[0]))
    for h, line in enumerate(lines):
        for w, char in enumerate(line):
            if char == ".":
                continue
            char_pos[char].append((h, w))

    anti_nodes = []
    combs = defaultdict(list)
    for char, positions in char_pos.items():
        print(f"\n---- {char} ----")
        print(f"positions: {positions}")
        if len(positions) > 1:
            for comb in combinations(positions, 2):
                combs[char].append(list(comb))

                diff = (comb[1][0] - comb[0][0], comb[1][1] - comb[0][1])

                print(f"{comb} -> diff: {diff}")
                adds = get_all_valid_tuples(comb[1], diff, board_size, "+")
                subs = get_all_valid_tuples(comb[0], diff, board_size, "-")
                print("adds", adds)
                print("subs", subs)
                for sub in subs:
                    if sub not in positions:
                        print(f"adding: {sub}")
                        anti_nodes.append(sub)

                for add in adds:
                    if add not in positions:
                        print(f"adding: {add}")
                        anti_nodes.append(add)

    print(len(set(anti_nodes)))

def debug():
    file = open("data/8.txt", "r")
    lines = [line.strip() for line in file.readlines()]
    for h, lines in enumerate(lines):
        for w, char in enumerate(lines):
            if char == "#":
                print(f"({h},{w})")


if __name__ == "__main__":
    main()
    # debug()