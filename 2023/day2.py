file = open("data/day2.txt", "r")
lines = file.readlines()

import re

cubes_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

total = 0

# part 1
for line in lines:
    line = line.strip()
    game_id = int(line.split(":")[0].replace("Game ", ""))
    game = []

    for set_ in line.split(":")[1].split(";"):
        game.append(set_.split(","))

    game_valid = []
    for set_ in game:
        for cubes in set_:
            cubes = cubes.strip()
            cube_amount, cube_color = cubes.split(" ")

            if int(cube_amount) > cubes_max[cube_color]:
                game_valid.append(False)
            else:
                game_valid.append(True)

    if all(game_valid):
        total += game_id


print("part 1:", total)


total = 0

# part 2
for line in lines:
    line = line.strip()
    game_id = int(line.split(":")[0].replace("Game ", ""))
    game = []

    for set_ in line.split(":")[1].split(";"):
        game.append(set_.split(","))

    colors = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for set_ in game:
        for cubes in set_:
            cubes = cubes.strip()
            cube_amount, cube_color = cubes.split(" ")
            cube_amount = int(cube_amount)

            if cube_amount > colors[cube_color]:
                colors[cube_color] = cube_amount

    total += colors["red"] * colors["green"] * colors["blue"]


print("part 2:", total)
