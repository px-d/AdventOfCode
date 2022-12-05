with open('01/input.txt') as f:
    elves_package = []
    elve = []
    for line in f.readlines():
        if line.strip():
            elve.append(line.strip())
        else:
            elves_package.append(elve)
            elve = []

    sums = [sum(map(int, p)) for p in elves_package]
    sums.sort()
    print(f"Task A: {sums[-1]}, Task B: {sum(list(sums[-1:-4:-1]))}")
