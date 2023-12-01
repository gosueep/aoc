file = open('input.txt', 'r')
lines = file.readlines()

convert = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

rps = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


def game(elf, me):
    if me == 'X':
        return 0 + rps[lose[elf]]
    if me == 'Y':
        return 3 + rps[convert[elf]]
    if me == 'Z':
        return 6 + rps[win[elf]]


score = 0
for line in lines:
    elf, me = line.split()

    score += game(elf, me)

print(score)
