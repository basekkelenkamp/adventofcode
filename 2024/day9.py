file = open("data/9.txt", "r")
string = file.read()


original_string = ""
block = True
_id = 0
for char in string:
    if not block:
        for j in range(int(char)):
            original_string += "."
        block = True
        continue
    for j in range(int(char)):
        original_string += str(_id)
        block = False
    _id += 1

print(f"start:\n{original_string}")


def move_block(blocks):
    # sort by dots last
    try:
        first_dot_index = blocks.index(".")
    except ValueError:
        return None
    for i, ch in enumerate(reversed(blocks)):
        i = (len(blocks) - i) - 1
        if ch == ".":
            continue
        else:
            blocks_list = list(blocks)
            blocks_list.pop(i)
            blocks_list[first_dot_index] = ch
            new_blocks = "".join(blocks_list)
            # print(new_blocks)
            return new_blocks


end = False
to_update = original_string
iteration = 0
while end is False:
    iteration += 1
    print(iteration)
    update = move_block(to_update)
    if update is None:
        end = True
    else:
        to_update = update

chars_no_dots = [int(char) for char in list(to_update) if char != "."]
print(sum([i*c for i, c in enumerate(chars_no_dots)]))
