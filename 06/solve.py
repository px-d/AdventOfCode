def packet(input, length):
    for i in range(len(input)):
        if (len(set(input[i:i + length])) == length):
            return i + length


if __name__ == '__main__':
    with open("06/input.txt") as f:
        line = f.readline()
        print(f"1: '{packet(line, 4)}', 2: '{packet(line, 14)}'")
