import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

seeds = list(map(int, lines[0].split()[1:]))
ranges = []
for i in range(0, len(seeds), 2):
    ranges.append((seeds[i], seeds[i] + seeds[i+1]))
print(ranges)

maps = []
curr = []
for line in lines[2:]:
    if line == '\n':
        # print(curr)
        maps.append(curr)
        curr = []
    if line[0].isnumeric():
        dest, src, l = map(int, line.split())
        curr.append((dest,src,l))
    # else:
    #     print(line)

maps.append(sorted(curr))
# print(maps)

for m in maps:
    # print('map', m)
    newseeds = []
    for start, end in ranges:
        modified = False
        for dest, src, l in m:
            if start <= src and src < end:
                newseeds.append((start, src-1))
                if end < src+l:
                    newseeds.append((dest, dest + end-src))
                else:
                    newseeds.append((dest, dest+l))
                    newseeds.append((src+l, end))
                # print(start,end, dest, src, l, newseeds)
                modified = True
            elif src <= start and start < src+l:
                shift = start-src
                if end <= src+l:
                    newseeds.append((dest + shift, dest + shift + end-start))
                else:
                    newseeds.append((dest + shift, dest + l)) 
                    newseeds.append((src+l, end))
                modified = True
        if not modified:
            newseeds.append((start,end))
    # print(ranges, '->',newseeds)
    ranges = newseeds
    # print()
                
# for i in range(len(seeds)):
#     s = seeds[i]
#     if src <= s and s < src+l and i not in modified:
#         seeds[i] = s-src + dest
#         modified.add(i)
# print(ranges)
print(sorted(ranges)[:30])
print(min(ranges))