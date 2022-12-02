
RPS_MAP = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

ACTION_MAP = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}


def load_data(path):
    d = []
    with open(path, 'r') as f:
        for li in f:
            line = li.replace("\n", "")
            line = line.replace(" ", "")
            tup = [letter for letter in line]
            d.append(tup)
    return d


def get_score(player1, action):

    # rock
    if player1 == "A":
        if action == "win":
            return 2 + 6
        elif action == "draw":
            return 1 + 3
        else:
            return 3 + 0

    # paper
    elif player1 == "B":
        if action == "win":
            return 3 + 6
        elif action == "draw":
            return 2 + 3
        else:
            return 1 + 0

    # scissors
    elif player1 == "C":
        if action == "win":
            return 1 + 6
        elif action == "draw":
            return 3 + 3
        else:
            return 2 + 0


def calc_score(player1, action):
    action = ACTION_MAP[action]
    return get_score(player1, action)


if __name__ == "__main__":
    data = load_data("2022/data/data_2.csv")
    result = 0
    for match in data:
        result += calc_score(match[0], match[1])
    print(result)
