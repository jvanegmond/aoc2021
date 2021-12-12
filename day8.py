with open("day8.txt") as file:
    input = file.read()

#input = "dcga cadgbfe gecba cbfde eda cdbea gbadfe fegcba bedgca da | bgefdac bdace ad agcd"

part1 = 0
part2 = 0

def num_matches(s1, s2):
    return len(set(s1) & set(s2))

def solve_part2(input, output):
    all_signals = input + output

    # Create empty dict for segments
    segments = {}
    for signal in range(9):
        segments[signal] = ""

    # Get the simple segments with a unique length
    for signal in all_signals:
        if len(signal) == 2:
            segments[1] = signal
        if len(signal) == 4:
            segments[4] = signal
        if len(signal) == 3:
            segments[7] = signal
        if len(signal) == 7:
            segments[8] = signal
    
    # Eliminate the remaining segments based on overlap with the simple segments
    for signal in all_signals:
        if len(signal) == 6:
            if num_matches(signal, segments[4]) == 4:
                segments[9] = signal
            elif num_matches(signal, segments[1]) == 1 or num_matches(signal, segments[7]) == 2:
                segments[6] = signal
            else:
                segments[0] = signal
        if len(signal) == 5:
            if num_matches(signal, segments[1]) == 2 or num_matches(signal, segments[7]) == 3:
                segments[3] = signal
            elif num_matches(signal, segments[6]) == 5 or num_matches(signal, segments[4]) == 3:
                segments[5] = signal
            else:
                segments[2] = signal
    
    # Replace individual output segments with numbers
    for o in range(len(output)):
        signal = output[o]
        for m in segments.keys():
            segment = segments[m]
            if len(segment) == len(signal) and num_matches(segment, signal) == len(signal):
                output[o] = m

    return int("".join(str(num) for num in output))

for line in input.splitlines():
    input, output = (part.split() for part in line.split("|"))
    part1 += len(list(filter(lambda x: len(x) in [2, 4, 3, 7], output)))
    part2 += solve_part2(input, output)

print("part 1", part1)
print("part 2", part2)