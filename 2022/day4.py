def load_data(path):
    with open(path, 'r') as f:
        count = 0
        for li in f:
            arr = li.strip().split(sep=",")
            strings = [a.split(sep="-") for a in arr]
            nums = [[int(num) for num in ar] for ar in strings]

            range1 = list(range(nums[0][0], nums[0][1] + 1))
            range2 = list(range(nums[1][0], nums[1][1] + 1))

            for e in range1:
                if e in range2:
                    count += 1
                    break

        return count


if __name__ == "__main__":
    data = load_data("2022/data/data_4.csv")
    print(data)
