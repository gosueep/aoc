file = open('input.txt', 'r')
lines = file.readlines()


elf = 0
elves = []
for line in lines:
    if line == '\n':
        elves.append(elf)
        elf = 0
    else:
        elf += int(line.strip())

print(max(elves))
