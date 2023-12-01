file = open('input.txt', 'r')
lines = file.readlines()

grid = []
for line in lines:
    grid.append([int(x) for x in line.strip()])

N = len(grid)


perim = (N * 2) + (N-2) * 2
trees = set()

for i in range(1, N-1):
    left = grid[i][0]
    j = 1
    while j < N-1:
        if grid[i][j] > left:
            trees.add((i, j))
            left = grid[i][j]
        j += 1

    right = grid[i][-1]
    j = N-1
    while j > 0:
        if grid[i][j] > right:
            trees.add((i, j))
            right = grid[i][j]
        j -= 1

for j in range(1,N-1):
    top = grid[0][j]
    i = 1
    while i < N-1:
        if grid[i][j] > top:
            trees.add((i, j))
            top = grid[i][j]
        i += 1

    tall = grid[-1][j]
    i = N-1
    while i > 0:
        if grid[i][j] > tall:
            trees.add((i, j))
            tall = grid[i][j]
        i -= 1

print(perim + len(trees))

