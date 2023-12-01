import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()


LOWER = 0
UPPER = 4000000
sensors = {}
intervals = [[] for i in range(UPPER+1)]


def addInterval(x, y_i, y_f):
    if y_i < 0:
        y_i = 0
    if y_f > UPPER:
        y_f = UPPER

    if LOWER <= x <= UPPER:
        intervals[x].append([y_i, y_f])


lnum = 0
for line in lines:
    lnum += 1
    print(lnum)

    line = line.strip().split()
    x = int(line[2][2:-1])
    y = int(line[3][2:-1])

    bx = int(line[-2][2:-1])
    by = int(line[-1][2:])

    d = abs(bx - x) + abs(by - y)

    addInterval(x, y-d, y+d)
    for dx in range(1, d):
        dy = d - dx
        addInterval(x-dx, y-dy, y+dy)
        addInterval(x+dx, y-dy, y+dy)


print()
print()

for coord, x in enumerate(intervals):
    x = sorted(x)

    start, end = x[0]
    for i, f in x[1:]:
        if start <= i <= end+1:
            end = max(end, f)
        else:
            print(coord, end+1)
            print(coord * UPPER + end+1)
            sys.exit()
