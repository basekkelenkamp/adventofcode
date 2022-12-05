import re


def load_data(path):
    with open(path, 'r') as f:
        indexes = [1, 5, 9, 13, 17, 21, 25, 29, 33]
        moves_ = []
        base_config = [0, [], [], [], [], [], [], [], [], []]
        init = True
        for line_count, li in enumerate(f, start=1):
            line = li.strip()
            if line_count == 9:
                init = False

            if init:
                for count, index in enumerate(indexes, start=1):
                    if line[index] != ' ':
                        base_config[count].append(line[index])
                continue

            if 'move' in line:
                moves_.append(line)
    return moves_, base_config


def move_containers(conf, amount, from_, to):
    conf[to][:0] = conf[from_][:amount]
    del conf[from_][:amount]
    return conf
    

if __name__ == "__main__":
    moves, config = load_data("2022/data/data_5.csv")
    for move in moves:
        reg = re.findall('\\d+', move)
        config = move_containers(config, int(reg[0]), int(reg[1]), int(reg[2]))

    answer = "".join([row[0] for row in config if isinstance(row, list)])
    print(answer)
