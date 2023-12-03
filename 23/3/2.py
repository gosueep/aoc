import sys
from collections import defaultdict

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

N = len(lines)

gears = defaultdict(list)

for i in range(N):
    onNum = False
    symbol = None
    for j in range(N):
        if onNum:
            if not lines[i][j].isnumeric() or j == N-1:
                onNum = False
                if lines[i][j].isnumeric() and j == N-1: 
                    num = int(lines[i][l:N])
                else:
                    num = int(lines[i][l:j])
                if symbol is not None:
                    # nums.append(num)
                    gears[symbol].append(num)
                    symbol = None
        elif lines[i][j].isnumeric():
            onNum = True
            l = j
            
        if onNum:
            for x, y in [(1,0), (-1,0), (0,1), (0,-1), 
                         (-1,-1), (-1,1), (1,-1), (1,1)]:
                ni, nj = i+x, j+y
                if ni >= 0 and ni < N and nj >= 0 and nj < len(lines[i]):
                    c = lines[ni][nj]
                    if c != '.' and not c.isnumeric():
                        symbol = (ni,nj)
        
total = 0
for i in gears:
    if len(gears[i]) > 1:    
        # print(gears[i])
        total += gears[i][0] * gears[i][1]
print(total)