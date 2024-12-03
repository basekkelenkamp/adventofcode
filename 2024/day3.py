file = open("data/3.txt", "r")
string = file.read()

result = 0
valid = False
dont = False
for i, char in enumerate(string):
    if string[i:i+7] == "don't()":
        print(string[i:i+7])
        dont = True
    if string[i:i+4] == 'do()':
        print(string[i:i+4])
        dont = False
    if dont:
        continue
    if not valid and not dont and string[i:i+4] == 'mul(' and string[i+4].isdigit():
        valid = True
        for i2, char2 in enumerate(string[i+4:]):
            if char2 == ')':
                nums = string[i+4:i+4+i2].split(',')
                if len(nums) == 2 and nums[0].isdigit() and nums[1].isdigit():
                    result += int(nums[0]) * int(nums[1])
                    valid = False
                    break
                break
    else:
        valid = False

print(result)
