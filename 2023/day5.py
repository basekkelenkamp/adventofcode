from pprint import pprint as pp
file = open("data/day5.txt", "r")
lines = file.readlines()


def consume_line(destination, source, range_len):
    source_range = range(int(source), int(source) + int(range_len))
    dest_range = range(int(destination), int(destination) + int(range_len))
    
    return source_range, dest_range


seeds = lines[0].split()[1:]
pp(f"seeds: {seeds}")

maps = {}
step_keys_order = []
for i, line in enumerate(line.strip() for line in lines):
    if i == 0 or i == 1:
        continue

    # create new map
    if i != 0 and ":" in line:
        new_map = {
            "sources_ranges": [],
            "destination_ranges": []
        }
        maps[line.split()[0]] = new_map
        step_keys_order.append(line.split()[0])
        continue

    if line == "":
        continue
    
    # consume line
    s_range, d_range = consume_line(*line.split())
    new_map["sources_ranges"].append(s_range)
    new_map["destination_ranges"].append(d_range)

print("maps:")
pp(maps)
pp("step_keys_order:")
pp(step_keys_order)

seed_locations = []
for seed in seeds:
    for step_key in step_keys_order:
        for i, source_range in enumerate(maps[step_key]["sources_ranges"]):
            if int(seed) in source_range:
                seed = maps[step_key]["destination_ranges"][i][source_range.index(int(seed))]
                break
    seed_locations.append(seed)


pp(f"lowest seed location: {min(seed_locations)}")