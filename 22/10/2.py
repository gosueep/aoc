file = open('input.txt', 'r')
lines = file.readlines()


H, W = 6, 40
screen = [['  ' for x in range(W)] for y in range(H)]


def iterate(i, col):
    row = i // W
    if col in [X - 1, X, X + 1]:
        screen[row][col] = '██'

    i += 1
    col = (col + 1) % W

    return i, col


X = 1
i = 0
col = 0
for line in lines:
    instr = line.split()

    i, col = iterate(i, col)

    if instr[0] != 'noop':
        i, col = iterate(i, col)
        add = int(instr[1])
        X += add

for row in screen:
    print(' '.join(row))

