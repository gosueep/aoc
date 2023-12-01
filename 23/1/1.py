import sys


FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

out = 0
for i in lines:
    curr = []
    for c in i:
        if c.isnumeric():
            curr.append(c)
    out += int(curr[0]+curr[-1])
    
print(out)