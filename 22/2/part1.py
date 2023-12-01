file = open('input.txt', 'r')
lines = file.readlines()

convert = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

rps = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


def game(elf, me):
    if convert[elf] == me:
        return 3
    if elf == 'A' and me == 'Y':
        return 6
    if elf == 'B' and me == 'Z':
        return 6
    if elf == 'C' and me == 'X':
        return 6
    return 0


score = 0
for line in lines:
    elf, me = line.split()

    score += rps[me]
    score += game(elf, me)

print(score)
