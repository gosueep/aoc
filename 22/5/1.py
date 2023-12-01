from collections import deque

file = open('input.txt', 'r')
lines = file.readlines()

N = 9
stacks = [ [] for x in range(N)]

for i,line in enumerate(reversed(lines[0:8])):
    for j in range(N):
        c = line[j*4+1]
        if c != ' ' and c != '':
            stacks[j].append(c)

stacks = [[]] + stacks

for s in stacks:
    print(s)

for line in lines[10:]:
    instr = line.split()

    amt = int(instr[1])
    src = int(instr[3])
    dest = int(instr[5])

    for i in range(amt):
        if stacks[src]:
            mv = stacks[src].pop()
            stacks[dest].append(mv)

    # print()
    # for s in stacks:
    #     print(s)
    # break

for i in stacks:
    if i:
        print(i[-1], end='')