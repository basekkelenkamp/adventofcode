file = open("data/2.txt", "r")
lines = file.readlines()

safe_reports = 0
for line in lines:
    li = list(map(lambda x: int(x), line.split(" ")))

    dampened_list = []
    added = False
    for i in range(len(li)):
        if added:
            break
        new_li = li.copy()
        new_li.pop(i)
        print(new_li)
        if new_li in [sorted(new_li), sorted(new_li, reverse=True)]:
            dampened_list = new_li
            for i2, num2 in enumerate(dampened_list):
                # stop at last element
                if i2 == len(dampened_list) - 1:
                    safe_reports += 1
                    added = True
                    break

                diff2 = abs(int(num2) - int(dampened_list[i2 + 1]))
                if diff2 > 3 or diff2 == 0:
                    break

print(safe_reports)
