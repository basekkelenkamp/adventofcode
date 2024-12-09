from itertools import product
file = open("7.txt", "r")
lines = [line.strip() for line in file.readlines()]

def evaluate_left_to_right(nums, operators):
    result = nums[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += nums[i + 1]
        elif op == "*":
            result *= nums[i + 1]
        elif op == "||":
            result = int(str(result) + str(nums[i + 1]))
    return result

count = 0
for line in lines:
    p1, p2 = line.split(":")
    result = int(p1)
    nums = [int(x) for x in p2.split(" ")[1:] if x.isdigit()]
    if len(nums) < 2 and result in [nums[0] * nums[1], nums[0] + nums[1]] or result == int(str(nums[0]) + str(nums[1])):
        count += result
        continue


    op_combinations = product(["+", "*", "||"], repeat=len(nums) - 1)
    for op_combination in op_combinations:
        res = evaluate_left_to_right(nums, op_combination)
        if res == result:
            count += result
            break


print(count)
