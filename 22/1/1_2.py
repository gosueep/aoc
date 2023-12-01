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

top3 = 0
for i in range(3):
    top = max(elves)
    elves.remove(top)
    top3 += top

print(top3)
