import sys
from collections import deque, defaultdict
import heapq
import math

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()


valves = {}
for line in lines:
    line = line.split()
    id = line[1]
    rate = -1 * int(line[4].split('=')[1][:-1])
    conns = []
    for x in line[9:]:
        conns.append(x.split(',')[0])
    valves[id] = (rate, conns)

print(valves)

adjList = defaultdict(list)
bfs = deque()
bfs.append((30, 'AA', set(), 0))
visited = set()
while bfs:
    t, c, state, rate = bfs.popleft()
    # print(t, c)
    if t >= 0 and (t, c) not in visited:
        visited.add((t,c))
        if c not in state:
            new_state = state.copy()
            new_state.add(c)
            bfs.append((t-1, c, new_state, rate + valves[c][0]))
            adjList[(t, c)].append((rate + valves[c][0], (t-1, c)))

        rate, neighbors = valves[c]
        for n in neighbors:
            bfs.append((t-1, n, state, rate))
            adjList[(t, c)].append((rate, (t-1, n)))

print(adjList)


dists = {}
unvisited = []

for node in adjList:
    dists[node] = math.inf
dists[(30, 'AA')] = 0
heapq.heappush(unvisited, (0, (30, 'AA')))

while unvisited:
    curr = heapq.heappop(unvisited)
    curr = curr[1]

    for weight, neighbor in adjList[curr]:
        time, n = neighbor
        if curr in dists and neighbor in dists:
            altDist = dists[curr] + weight
            if altDist < dists[neighbor]:
                dists[neighbor] = altDist
                heapq.heappush(unvisited, (altDist, neighbor))

print(dists)
print(min(dists), dists[min(dists)])

