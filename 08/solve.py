lines = [x.strip() for x in open("08/input.txt")]
height = len(lines)
matrix = [list(x) for x in lines]

print(matrix)

# By starting with the offset, we guarantee that we
# always have elements surrounding all others
visible = (len(matrix)-1) * 4
print(f"Visible initially= {visible}")
for x in range(1, len(matrix) - 1):
    for y in range(1, len(matrix) - 1):
        ...


def all_smaller(matrix, starting_point: tuple):
    x, y = starting_point
    visible = 0
    # From X,Y > UP
    if all([int(matrix[x][xx]) < int(matrix[x][y]) for xx in range(0, y - 1)]):
        visible += 1
        print(f"{x}/{y}")
    # From X,Y > DOWN
    if all([int(matrix[x][xx]) < int(matrix[x][y]) for xx in range(y+1, height)]):
        visible += 1
    return visible
    


print(all_smaller(matrix, (2, 2)))
