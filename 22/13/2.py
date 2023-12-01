import functools
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


packets = [[[2]], [[6]]]
for line in lines:
    if line.strip() != "":
        packets.append(ast.literal_eval(line))

s = sorted(packets, key=functools.cmp_to_key(inOrder), reverse=True)

two = s.index([[2]])+1
six = s.index([[6]])+1
print(f'{two} * {six} = {two * six}')

