import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()


time = int(''.join(lines[0].split()[1:]))
dist = int(''.join(lines[1].split()[1:]))

total = 1
wins = 0
for h in range(time):
    d = (time-h)*h
    if d > dist:
        wins += 1
print(wins)