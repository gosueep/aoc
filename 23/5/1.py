import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

seeds = list(map(int, lines[0].split()[1:]))

modified = set()

for line in lines:
    if line[0].isnumeric():
        dest, src, l = map(int, line.split())
        print(dest, src, l)
        for i in range(len(seeds)):
            s = seeds[i]
            if src <= s and s < src+l and i not in modified:
                print(s, "IN RANGE", src, src+l)
                print(s, '->', s-src + dest)
                seeds[i] = s-src + dest
                modified.add(i)
        print(seeds)
    else:
        print(line)
        modified.clear()

print(seeds)
print(min(seeds))

