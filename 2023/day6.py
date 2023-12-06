from pprint import pprint as pp
file = open("data/day6.txt", "r")
lines = file.readlines()


# part1
# def split_numbers(line):
#     spl = line.split()
#     return [int(s) for s in spl[1:]]

# times = []
# records = []
# for line in lines:
#     if line.startswith("Time:"):

#         times = split_numbers(line)

#     if line.startswith("Distance:"):
#         records = split_numbers(line)

# num_wins = []
# for time, record in zip(times, records):
#     race_wins = 0
#     for speed in range(1, time):
#         time_left = time - speed
#         distance = speed * time_left
#         if distance > record:
#             race_wins += 1
#     num_wins.append(race_wins)

# pp(f"num_wins: {num_wins}")
# pp(f"Multiplied: {num_wins[0] * num_wins[1] * num_wins[2] * num_wins[3]}")


# part2
def combine_numbers(line):
    return int("".join(char for char in line if char.isdigit()))

time = 0
record = 0
for line in lines:
    if line.startswith("Time:"):
        time = combine_numbers(line)
    elif line.startswith("Distance:"):
        record = combine_numbers(line)

pp(f"Time: {time}")
pp(f"Record: {record}")

race_wins = 0
for speed in range(1, time):
    time_left = time - speed
    distance = speed * time_left
    if distance > record:
        race_wins += 1
    elif distance <= record and race_wins != 0:
        break

pp(f"race_wins: {race_wins}")
