with open("day9.txt") as file:
    input = file.read()

map = list(list(list(int(elem) for elem in str) for str in input.splitlines()))
map_size_x = len(map)
map_size_y = len(map[0])

def neighbors(x, y):
    if x > 0:
        yield (x - 1, y)
    if x < map_size_x - 1:
        yield (x + 1, y)
    if y > 0:
        yield (x, y - 1)
    if y < map_size_y - 1:
        yield (x, y + 1)

def neighbor_values(x, y):
    for x, y in neighbors(x, y):
        yield map[x][y]

# Part 1
risk_level = 0
for x in range(map_size_x):
    for y in range(map_size_y):
        if map[x][y] < min(neighbor_values(x, y)):
            risk_level += 1 + map[x][y]

print("part 1", risk_level)

# Part 2
basin = list(([-1] * map_size_y) for r in range(map_size_x))
cur_basin = 0
basin_size = {}

def fill_basin(x, y):
    if map[x][y] == 9: return

    for x, y in neighbors(x, y):
        if map[x][y] == 9:
            continue
        if basin[x][y] == -1:
            basin[x][y] = cur_basin
            basin_size[cur_basin] += 1
            fill_basin(x, y)

for x in range(map_size_x):
    for y in range(map_size_y):
        if basin[x][y] == -1 and map[x][y] != 9:
            cur_basin += 1
            basin_size[cur_basin] = 0
            fill_basin(x, y)

sizes = list(basin_size.values())
sizes.sort(reverse=True)
print("part 2", sizes[0] * sizes[1] * sizes[2])