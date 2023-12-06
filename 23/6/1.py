import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()


times = list(map(int, lines[0].split()[1:]))
dists = list(map(int, lines[1].split()[1:]))

total = 1
for i in range(len(times)):
    l = times[i]
    wins = []
    for h in range(times[i]):
        d = (l-h)*h
        if d  > dists[i]:
            wins.append(d)
    print(wins)
    total *= len(wins)
print(total)