from itertools import islice


def signal_length(input, length):
    for i in range(len(input)):
        if (len(set(input[i:i + length])) == length):
            return i + length


with open("06/input.txt") as f:
    line = f.readline()
    print(f"1: {signal_length(line, 4)}, 2: {signal_length(line, 14)}")
