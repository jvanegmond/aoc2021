with open("day10.txt") as file:
    input = file.read()

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

# Part 1

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

file_score = 0
correct = [] # Collect lines without error for part 2
for line in input.splitlines():
    stack = []
    line_score = 0
    for char in list(line):
        open_pair = pairs.get(char)
        if open_pair is not None:
            stack.append(open_pair)
        else:
            expect = stack.pop()
            if char == expect:
                continue
            else:
                #print(f"Expected {expect}, but found {char} instead.")
                line_score += points[char]
                break
    if line_score == 0:
        correct.append(line)
    file_score += line_score

print("part1", file_score)

# Part 2

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

scores = []
for line in correct:
    stack = []
    for char in list(line):
        open_pair = pairs.get(char)
        if open_pair is not None:
            stack.append(open_pair)
        else:
            expect = stack.pop()
    # calculate score based on stack
    line_score = 0
    stack.reverse()
    for char in stack:
        line_score *= 5
        line_score += points[char]
    scores.append(line_score)

scores.sort()
print("part2", scores[len(scores) // 2])