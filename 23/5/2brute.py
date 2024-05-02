import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

seeds = list(map(int, lines[0].split()[1:]))


maps = []
curr = []
for line in lines[2:]:
    if line == '\n':
        maps.append(curr)
        curr = []
    if line[0].isnumeric():
        dest, src, l = map(int, line.split())
        curr.append((dest,src,l))
        

# print(seeds)
lowest = int(1e15)
for i in range(0,len(seeds), 2):
    for j in range(seeds[i], seeds[i]+seeds[i+1]):
        s = j
        for m in maps:
            for dest, src, l in m:
                if src <= s and s < src+l:
                    s = s-src + dest
                    break
        lowest = min(lowest, s)
        
print(lowest)
        
