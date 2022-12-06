from itertools import islice


def window(iterable, size):
    return zip(*[islice(iterable, s, None) for s in range(size)])


def all_individual(iterable):
    # This could probably be a one-liner
    for idx1, x in enumerate(iterable):
        for idx2, y in enumerate(iterable):
            if x == y and idx1 != idx2:
                return False
    return True


def signal_length(input, length):
    for idx, frame in enumerate(list(window(input, length))):
        if all_individual(frame):
            return idx+length
    return -1


with open("06/input.txt") as f:
    line = f.readline()
    print(f"1: {signal_length(line, 4)}, 2: {signal_length(line, 14)}")

