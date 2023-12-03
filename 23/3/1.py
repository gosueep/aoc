import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

N = len(lines)

nums = []

for i in range(N):
    onNum = False
    symbol = False
    for j in range(N):
        if onNum:
            if not lines[i][j].isnumeric() or j == N-1:
                onNum = False
                if lines[i][j].isnumeric() and j == N-1: 
                    num = int(lines[i][l:N])
                else:
                    num = int(lines[i][l:j])
                print(num, symbol)
                if symbol:
                    nums.append(num)
                    symbol = False   
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
                        symbol = True
        
print(nums)
print(sum(nums))