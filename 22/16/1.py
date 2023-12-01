import sys
import heapq, math
import copy

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

# print(valves)


dp = {}
def maxpress(mins_left, v, rate, total, opened):

    # opened = opened.copy()

    if mins_left == 1:
        dp[(mins_left, v)] = (total + rate, opened)
        return dp[(mins_left, v)]

    if (mins_left, v) in dp:
        return dp[(mins_left, v)]

    options = []
    if v not in opened:
        # new_state = copy.deepcopy(opened)
        new_state = opened.copy()
        new_state.add(v)
        new_rate = rate + valves[v][0]
        options.append(maxpress(mins_left - 1, v, new_rate, total + new_rate, new_state))
    for n in valves[v][1]:
        options.append(maxpress(mins_left - 1, n, rate, total + rate, opened))

    print(mins_left, v, options)
    best = max(options, key=lambda x: x[0])
    print(total, best)
    dp[(mins_left, v)] = best
    return dp[(mins_left, v)]


x, op = maxpress(30, 'AA', 0, 0, set())
print(op)
print(x)

print(dp)
# print(dp[30, 'AA'])
