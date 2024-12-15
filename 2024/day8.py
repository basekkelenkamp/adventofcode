from itertools import combinations
from collections import defaultdict


def add_tuple(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def add_tuples(t1, diff, board_size):
    tuples = []
    while True:
        t1 = add_tuple(t1, diff)
        if 0 <= t1[0] < board_size[0] and 0 <= t1[1] < board_size[1]:
            tuples.append(t1)
        else:
            break
    return tuples


def subtract_tuple(t1, t2):
    return t1[0] - t2[0], t1[1] - t2[1]


def subtract_tuples(t1, diff, board_size):
    tuples = []
    while True:
        t1 = subtract_tuple(t1, diff)
        if 0 <= t1[0] < board_size[0] and 0 <= t1[1] < board_size[1]:
            tuples.append(t1)
        else:
            break
    return tuples


def main():
    file = open("data/8.txt", "r")
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
            anti_nodes.extend(positions)
            for comb in combinations(positions, 2):
                combs[char].append(list(comb))

                diff = (comb[1][0] - comb[0][0], comb[1][1] - comb[0][1])

                print(f"{comb} -> diff: {diff}")
                adds = add_tuples(comb[1], diff, board_size)
                subs = subtract_tuples(comb[0], diff, board_size)
                # adds_subs = set()
                # adds_subs.update(adds)
                # adds_subs.update(subs)
                anti_nodes.extend(adds)
                anti_nodes.extend(subs)


                # print(f"adds: {adds}, subs: {subs}")
                # if 0 <= sub[0] < board_size[0] and 0 <= sub[1] < board_size[1] and sub not in positions:
                #     print(f"adding (sub): {sub}")
                #     anti_nodes.append(sub)
                #
                # if 0 <= add[0] < board_size[0] and 0 <= add[1] < board_size[1] and add not in positions:
                #     print(f"adding (add): {add}")
                #     anti_nodes.append(add)

    print(len(set(anti_nodes)))
    # print
    for h, line in enumerate(lines):
        for w, char in enumerate(line):
            if (h, w) in anti_nodes:
                print("#", end="")
            else:
                print(char, end="")
        print()


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