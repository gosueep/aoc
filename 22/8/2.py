file = open('input.txt', 'r')
lines = file.readlines()

grid = []
for line in lines:
    grid.append([int(x) for x in line.strip()])

N = len(grid)


def score(arr, i):
    if i == 0 or i == N-1:
        return 0

    curr = arr[i]

    left = 1
    j = i-1
    while j > 0 and arr[j] < curr:
        left += 1
        j -= 1

    right = 1
    j = i+1
    while j < N-1 and arr[j] < curr:
        right += 1
        j += 1

    return left * right


best = -1
for i in range(1, N-1):
    for j in range(1, N-1):

        lr = score(grid[i], j)
        ud = score([row[j] for row in grid], i)

        total = lr * ud
        if total > best:
            best = total

print(best)

