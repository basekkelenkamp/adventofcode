
def load_data(path):
    with open(path, 'r') as f:
        for line in f:
            return line


if __name__ == "__main__":
    data = load_data("2022/data/data_6.csv")
    marker = []
    for index, letter in enumerate(data):
        if letter not in marker:
            marker.append(letter)
        else:
            marker = marker[marker.index(letter)+1:]
            marker.append(letter)

        # change to 4 for part1, it still works :D
        if len(marker) == 14:
            print(marker, index+1)
