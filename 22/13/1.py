import sys
import ast

sys.setrecursionlimit(2 ** 30)

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()


def inOrder(left, right):

    # check order
    for i in range(min(len(left), len(right))):
        l = left[i]
        r = right[i]

        if type(l) == int and type(r) == int:
            if l < r:
                return 1
            elif l > r:
                return -1
        else:
            if type(l) == int:
                l = [l]
            elif type(r) == int:
                r = [r]

            suborder = inOrder(l, r)
            if suborder != 0:
                return suborder

    if len(left) > len(right):
        return -1
    elif len(left) < len(right):
        return 1

    return 0


ans = 0
pairs = []
pairnum = 1
for i in range(0, len(lines), 3):

    left = ast.literal_eval(lines[i])
    right = ast.literal_eval(lines[i+1])

    if inOrder(left, right) == 1:
        ans += pairnum
        pairs.append(pairnum)

    pairnum += 1

print(pairs)
print(ans)

