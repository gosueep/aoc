import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

instr = lines[0].strip()

move = {}
for line in lines[2:]:
    m = line.split()
    src = m[0]
    l = m[2][1:-1]
    r = m[3][:-1]
    move[src] = (l,r)


curr = []
for s in move:
    if s[-1] == 'A':
        curr.append(s)

print(curr)

i = 0
while True:
    dir = instr[i%len(instr)]
    allZ = True
    newcurr = []
    for c in curr:
        c = move[c][dir == 'R']
        if c[-1] != 'Z':
            allZ = False
        newcurr.append(c)
    print(curr, newcurr)
    i += 1
    if allZ:
        break  
    curr = newcurr
print(i)