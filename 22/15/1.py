import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()


Y_POS = 2000000
yline = set()
beacons = set()
for linenum, line in enumerate(lines):
    print(f'Line: {linenum+1}')
    line = line.strip().split()
    x = int(line[2][2:-1])
    y = int(line[3][2:-1])
    if y == Y_POS and (x, y) not in beacons:
        yline.add(x)

    bx = int(line[-2][2:-1])
    by = int(line[-1][2:])
    beacons.add((bx, by))

    d = abs(bx - x) + abs(by - y)
    for i in range(x-d, x+d):
        if (i, Y_POS) not in beacons and abs(i - x) + abs(Y_POS - y) <= d:
            yline.add(i)


print(len(yline))