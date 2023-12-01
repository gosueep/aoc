file = open('input.txt', 'r')
lines = file.readlines()


X = 1
sigs = 0
i = 0

for line in lines:
    i += 1
    instr = line.split()

    if i % 40 == 20:
        sigs += i * X

    if instr[0] != 'noop':
        add = int(instr[1])
        i += 1
        if i % 40 == 20:
            sigs += i * X
        X += add


print(sigs)
