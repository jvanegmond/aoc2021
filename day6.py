# Go get some coffee
fishes = [1,4,1,1,1,1,1,1,1,4,3,1,1,3,5,1,5,3,2,1,1,2,3,1,1,5,3,1,5,1,1,2,1,2,1,1,3,1,5,1,1,1,3,1,1,1,1,1,1,4,5,3,1,1,1,1,1,1,2,1,1,1,1,4,4,4,1,1,1,1,5,1,2,4,1,1,4,1,2,1,1,1,2,1,5,1,1,1,3,4,1,1,1,3,2,1,1,1,4,1,1,1,5,1,1,4,1,1,2,1,4,1,1,1,3,1,1,1,1,1,3,1,3,1,1,2,1,4,1,1,1,1,3,1,1,1,1,1,1,2,1,3,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,5,1,1,1,2,2,1,1,3,5,1,1,1,1,3,1,3,3,1,1,1,1,3,5,2,1,1,1,1,5,1,1,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,5,1,4,3,3,1,3,4,1,1,1,1,1,1,1,1,1,1,4,3,5,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,2,1,4,4,1,1,1,1,1,1,1,5,1,1,2,5,1,1,4,1,3,1,1]
days = 80

for day in range(days):
    new_fishes = 0
    for n in range(len(fishes)):
        if fishes[n] == 0:
            new_fishes += 1
            fishes[n] = 6
        else:
            fishes[n] -= 1
    fishes += [8] * new_fishes
    print("day", day, "fishes", len(fishes))

print("solution =", len(fishes))