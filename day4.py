import os

with open("day4.txt") as file:
    input = file.read()

class Bingo(BaseException):
    board: "Board"
    move: int
    def __init__(self, board, move):
        self.board = board
        self.move = move

class Board:
    mask: int = 0xFF # 255

    def __init__(self, boardstr: str):
        self.numbers = list(int(move) for move in boardstr.split())

    def get_row(self, rownum):
        rownum *= 5
        return self.numbers[rownum:rownum+5]
    
    def get_column(self, colnum):
        return self.numbers[colnum:(colnum+5)*5:5]

    def get_rows_and_columns(self):
        for n in range(4):
            yield self.get_row(n)
            yield self.get_column(n)

    def mark(self, num: int):
        try:
            n = self.numbers.index(num)
            self.numbers[n] += self.mask + 1
        except ValueError:
            pass

        for row_or_column in self.get_rows_and_columns():
            if all((elem >= self.mask) for elem in row_or_column):
                raise Bingo(self, move) # !!!

    def get_unmarked(self):
        return filter(lambda number: number < self.mask, self.numbers)

    def wipe(self):
        self.numbers = list(number & self.mask for number in self.numbers)

input = input.split("\n\n")
moves = list(int(move) for move in input[0].split(","))

boards = []
for n in range(1, len(input)):
    boards.append(Board(input[n]))

# Part 1
# Upon getting Bingo!, it must be loudly proclaimed. Mumbling or muttering is against the rules and no prizes may be claimed.
try:
    for move in moves:
        for board in boards:
            board.mark(move)
except Bingo as b:
    print("part 1 =", sum(b.board.get_unmarked()) * b.move)

list(board.wipe() for board in boards)

# Part 2
for move in moves:
    for board in boards.copy():
        try:
            board.mark(move)
        except Bingo:
            if len(boards) == 1:
                print("part 2 =", sum(boards[0].get_unmarked()) * move)
                exit()
            boards.remove(board)