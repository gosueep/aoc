import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

red=12
green=13
blue=14
out = 0
for line in lines:
    # print(line.split())
    game = line.split()
    id = int(game[1][:-1])
    game = game[2:]
    r=0
    g=0
    b=0
    possible = True
    for i in range(0,len(game), 2):
        num = int(game[i])
        color = game[i+1]
        if color.startswith('red'): 
            r = max(r, num)
        elif color.startswith('green'): 
            g = max(g, num)
        elif color.startswith('blue'): 
            b = max(b, num)
        
    out += r*g*b
print(out)