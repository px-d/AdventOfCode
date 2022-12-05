with open('04/input.txt', 'r') as f:
    lines = f.read().splitlines()

    fully_encased, partially_encased = 0, 0
    for l in lines:
        a = l.split(',')[0].split('-')
        b = l.split(',')[1].split('-')
        set_a, set_b = set(range(int(a[0]), int(a[1])+1)),
        set(range(int(b[0]), int(b[1])+1))

        if set_a.issubset(set_b):
            fully_encased += 1
        elif set_a.intersection(set_b):
            partially_encased += 1

print(f"Fully encased: {fully_encased}")
print(f"Partially encased: {partially_encased + fully_encased}")
