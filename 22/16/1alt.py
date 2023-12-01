import sys
from collections import deque

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()


valves = {}
for line in lines:
    line = line.split()
    id = line[1]
    rate = int(line[4].split('=')[1][:-1])
    conns = []
    for x in line[9:]:
        conns.append(x.split(',')[0])
    valves[id] = (rate, conns)


dfs = deque()
dfs.append('AA')
while dfs:
    c = dfs.pop()
    if
    for n in valves[c]:
        dfs.append(n)


