def half(input):
    return input[:len(input)//2], input[len(input)//2:]


if __name__ == '__main__':
    
    weights = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    common_chars = {}
    prio = 0
    with open("03/input.txt") as f:
        input = f.read().splitlines()
        
        # Part 1
        for l in input:
            halves = half(l)
            for char in halves[0]:
                if char in halves[1]:
                    prio += weights.index(char) + 1
                    break
        
        # Part 2
        teams = [input[x:x+3] for x in range(0, len(input), 3)]
        prio_b = 0
        for team in teams:
            for char in team[0]:
                if char in team[1] and char in team[2]:
                    prio_b += weights.index(char) + 1
                    break
                    
        print(f"Part 1: {prio}")
        print(f"Part 2: {prio_b}")
        
        