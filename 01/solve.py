def main():

    elves_package = []

    with open('01_12/input.txt') as f:
        elve = []
        for line in f.readlines():
            if line.strip():
                elve.append(line.strip())
            else:
                elves_package.append(elve)
                elve = []

        sums = [sum(map(int, p)) for p in elves_package]
        largest = (0, 0)
        for idx, amount in enumerate(sums):
            if amount > largest[0]:
                largest = amount, idx

        print(f"Elve {largest[1]+1} has the largest package with {largest[0]}")
        
        # Part 2
        # Total of the top 3 elves
        sums.sort(reverse=True)
        print(sum(list(sums[:3])))
        
        
if __name__ == '__main__':
    main()
