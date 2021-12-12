from typing import Iterable

with open("day5.txt") as file:
    input = file.read()

# Parse input
board_size = 1000

points = []

class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def from_str(cls, str: str):
        return cls(*(int(x) for x in str.split(",")))

for i in input.splitlines():
    i = i.split(" -> ")
    p1 = Point.from_str(i[0])
    p2 = Point.from_str(i[1])
    points.append((p1, p2))

# Part 1

board = [ [0]*board_size for i in range(board_size)]

def _range(start, end) -> Iterable[int]:
    step = 1 if end >= start else -1
    return range(start, end + step, step)

for (p1, p2) in points:
    if p1.x == p2.x:
        for y in _range(p1.y, p2.y):
            board[p1.x][y] += 1
    elif p1.y == p2.y:
        for x in _range(p1.x, p2.x):
            board[x][p1.y] += 1

print("part 1 = ", sum(len(list(filter(lambda x: x > 1, row))) for row in board))

# Part 2

def diagonal_line(p1, p2) -> Iterable[Point]:
    xrange = _range(p1.x, p2.x)
    yrange = _range(p1.y, p2.y)

    for n in range(len(xrange)):
        yield Point(xrange[n], yrange[n])


for (p1, p2) in points:
    # Horizontal and vertical lines were already marked in part 1
    if p1.x != p2.x and p1.y != p2.y:
        for pos in diagonal_line(p1, p2):
            board[pos.x][pos.y] += 1

print("part 2 = ", sum(len(list(filter(lambda x: x > 1, row))) for row in board))