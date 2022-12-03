alphabet = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def load_data(path):
    total = 0
    with open(path, 'r') as f:
        group = []
        for li in f:

            line = li.replace("\n", "")
            group.append(line)

            if len(group) == 3:
                for letter in group[0]:
                    if letter in group[1] and letter in group[2]:
                        total += alphabet.index(letter)
                        group = []
                        break
    return total


if __name__ == "__main__":
    data = load_data("2022/data/data_3.csv")
    print(data)
