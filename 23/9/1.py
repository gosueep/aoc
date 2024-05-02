import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()


out = 0
for line in lines:
    nums = list(map(int, line.split()))

    hist = [nums]
    while True:
        curr = hist[-1]
        diff = []
        for i in range(1, len(curr)):
            diff.append(curr[i] - curr[i-1])

        hist.append(diff)
        if len(set(diff)) == 1:
            break

    
    h = sum(x[-1] for x in hist)
    out += h

print(out)
