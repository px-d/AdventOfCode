#  Me:   X for Rock, Y for Paper, and Z for Scissors.
#  Elve: A for Rock, B for Paper, and C for Scissors.

weight = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3
}

translated = {
    "X": "A",
    "Y": "B",
    "Z": "C",
    "A": "X",
    "B": "Y",
    "C": "Z",
}

win = {
    "A": "B",
    "B": "C",
    "C": "A",
}

loose = {
    "A": "C",
    "B": "A",
    "C": "B",
}

with open("02/input.txt") as f:
    rounds = f.read().splitlines()
    my_score = 0
    score = 0
    for round in rounds:
        elve = round[0]
        me = round[2]

        my_score += weight[me]

        if me == translated[elve]:
            my_score += 3

        if (me == "X" and elve == "C") or (me == "Y" and elve == "A") or (me == "Z" and elve == "B"):
            my_score += 6
    
        if me == "Z":
            win_move = win[elve]
            score += 6 + weight[win_move]
        elif me == "Y":
            draw_move = elve
            score += 3 + weight[draw_move]
        elif me == "X":
            loose_move = loose[elve]
            score += weight[loose_move]
            
    print(f"Task 1: {my_score}")
    print(f"Task 2: {score}")