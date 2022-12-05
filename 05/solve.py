def move_crate(amount, go, to, crates):
    for _ in range(0, amount):
        crates[to].append(crates[go].pop())
    return crates

def move_crate_v2(amount, go, to, crates):
    to_move = crates[go][-amount:]
    del crates[go][-amount:]
    for x in to_move:
        crates[to].append(x)

version = "v2"

with open('05/input.txt') as f:
    lines = f.read().rstrip().splitlines()

    pyramid = []
    crates = {}

    for l in lines:
        if not l:
            for idx in pyramid[len(pyramid)-1]:
                crates[idx] = list(filter(None, [pyramid[x][int(idx)-1]
                                   for x in range(0, len(pyramid) - 1)][::-1]))
        elif l.startswith("move"):
            a, b, c = l.replace("move ", "").replace(
                " from ", ",").replace(" to ", ",").split(",")
            if version == "v1":
                move_crate(int(a), b, c, crates)
            else:
                move_crate_v2(int(a), b, c, crates)
        else:
            pyramid.append(l.replace("[", "").replace("]", "").replace("    ", ",").replace("   ", ",").strip().replace(
                " ", ",").split(","))
    
    # Print Solution!
    for x in crates.items():
        print(x[1][-1], end=" ")