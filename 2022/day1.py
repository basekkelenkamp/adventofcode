

def load_data(path):
    d = []
    with open(path, 'r') as f:
        for li in f:
            line = li.replace("\n", "")
            if line:
                int(line)
            d.append(line)
    return d


if __name__ == "__main__":
    data = load_data("2022/data/data_1.csv")

    all_food = []
    foods = 0
    for food in data:
        if not food:
            all_food.append(foods)
            foods = 0
            continue
        foods += int(food)

    all_food.sort()
    
    answer_1 = all_food[-1]
    print(f"part 1: {answer_1}")

    answer_2 = all_food[-1] + all_food[-2] + all_food[-3]
    print(f"part 2: {answer_2}")
