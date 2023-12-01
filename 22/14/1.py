import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

left = 0
right = 0

cave = set()
for line in lines:
    line = line.strip().split(' -> ')
    for pos in range(1, len(line)):
        old_i, old_j = map(int, line[pos-1].split(','))
        new_i, new_j = map(int, line[pos].split(','))
        cave.add((old_i, old_j))
        cave.add((new_i, new_j))
        if old_i == new_i:
            a, b = sorted([old_j, new_j])
            for j in range(a, b):
                cave.add((old_i, j))
        if old_j == new_j:
            a, b = sorted([old_i, new_i])
            for i in range(a, b):
                cave.add((i, old_j))

beforeSand = len(cave)
src = (500, 0)
left = min(cave)[0]
right = max(cave)[0]


def fall(i, j):
    if i < left or i > right:
        return True

    while (i, j) not in cave:
        j += 1

    if (i-1, j) not in cave:
        return fall(i-1, j)
    elif (i+1, j) not in cave:
        return fall(i+1, j)
    else:
        cave.add((i, j-1))


while src not in cave:
    i, j = src
    if fall(i, j):
        break

print(beforeSand)
print(len(cave))
print(len(cave) - beforeSand)