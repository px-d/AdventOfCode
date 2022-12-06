from itertools import islice


def frame(input, length):
    for i in range(len(input)):
        if (len(set(input[i:i + length])) == length):
            return i + length


with open("06/input.txt") as f:
    line = f.readline()
    print(f"1: {frame(line, 4)}, 2: {frame(line, 14)}")
