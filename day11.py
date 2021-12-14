input = """6744638455
3135745418
4754123271
4224257161
8167186546
2268577674
7177768175
2662255275
4655343376
7852526168"""

board = list(list(int(char) for char in list(line)) for line in input.splitlines())
grid_size = len(board[0])
max_steps = 300
total_flashes = 0

def neighbors(x, y):
    for nx in range(x-1, x+2):
        for ny in range(y-1, y+2):
            if nx == x and ny == y: continue

            if nx >= 0 and nx < grid_size and ny >= 0 and ny < grid_size:
                yield (nx, ny)

def maybe_flash(x, y):
    global total_flashes
    if board[x][y] <= 9: return
    total_flashes += 1
    board[x][y] = -100
    for (nx, ny) in neighbors(x, y):
        board[nx][ny] += 1
        maybe_flash(nx, ny)

for step in range(1, max_steps):
    turn_flashes = total_flashes
    for x in range(grid_size):
        for y in range(grid_size):
            board[x][y] += 1
    
    for x in range(grid_size):
        for y in range(grid_size):
            maybe_flash(x, y)
    
    for x in range(grid_size):
        for y in range(grid_size):
            if board[x][y] < 0: board[x][y] = 0
    
    turn_flashes = total_flashes - turn_flashes

    if turn_flashes == (grid_size * grid_size):
        print("part 2", step)
        break
    
    if step == 100:
        print("part 1", total_flashes)