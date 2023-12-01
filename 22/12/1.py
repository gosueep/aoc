import sys
from collections import defaultdict, deque

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'
    print('RUNNING TEST INPUT')
else:
    print('RUNNNING REAL INPUT')

file = open(FILENAME, 'r')
lines = file.readlines()


grid = []
for line in lines:
    grid.append([x for x in line.strip()])


start = ()
end = ()
adjList = defaultdict(list)
for i, line in enumerate(grid):
    for j, node in enumerate(line):

        if node == 'S':
            start = (i, j)
            elev = ord('a')
        elif node == 'E':
            end = (i, j)
            elev = ord('z')
        else:
            elev = ord(node)

        for new_i, new_j in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
            if 0 <= new_i < len(lines) and 0 <= new_j < len(line):
                if grid[new_i][new_j] == 'S':
                    new_elev = ord('a')
                elif grid[new_i][new_j] == 'E':
                    new_elev = ord('z')
                else:
                    new_elev = ord(grid[new_i][new_j])

                if new_elev - elev <= 1:
                    adjList[(i, j)].append((new_i, new_j))


parent = dict()
visited = set()
bfs = deque()
bfs.append(start)
visited.add(start)
while bfs:
    curr = bfs.popleft()
    if curr == end:
        break
    for n in adjList[curr]:
        if n not in visited:
            bfs.append(n)
            visited.add(n)
            parent[n] = curr

path = deque()
curr = end
while curr != start:
    path.appendleft(curr)
    curr = parent[curr]

print(len(list(path)))