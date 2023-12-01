from collections import defaultdict
import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()


def parseOp(operation):
    op = operation.split()
    if op[-2] == '+':
        return '+', int(op[-1])
    elif op[-2] == '*':
        if op[-1] == 'old':
            return '**', 2
        else:
            return '*', int(op[-1])


class Monkey:
    def __init__(self, items, op, div, test_true, test_false):
        self.items = items
        self.op_type, self.op_num = parseOp(op)

        self.div = div
        self.test_true = test_true
        self.test_false = test_false

        self.inspected = 0

    def operate(self, level):
        if self.op_type == '*':
            return level * self.op_num
        elif self.op_type == '+':
            return level + self.op_num
        elif self.op_type == '**':
            return level ** self.op_num


    def turn(self):
        updates = defaultdict(list)
        self.inspected += len(self.items)
        for wlevel in self.items:
            wlevel = self.operate(wlevel)
            wlevel = wlevel % MOD

            if wlevel % self.div == 0:
                updates[self.test_true].append(wlevel)
            else:
                updates[self.test_false].append(wlevel)

        self.items = []
        return updates


monkeys = []
MOD = 1
for l in range(0, len(lines), 7):
    # Line 1 - Items
    items = lines[l+1].strip().split('Starting items: ')[1]
    items = list(map(int, items.strip().split(',')))

    # Line 2 - Operation
    op = lines[l+2].strip().split('Operation: ')[1]

    # Lines 3-5 - Test
    div = int(lines[l+3].strip().split()[-1])               # Line 3 - divisor
    test_true = int(lines[l+4].strip().split()[-1])         # Line 4 - if true
    test_false = int(lines[l + 5].strip().split()[-1])      # Line 5 - if false

    monkeys.append(Monkey(items, op, div, test_true, test_false))
    MOD *= div


for i in range(10000):
    for m in monkeys:
        updates = m.turn()
        for u in updates:
            monkeys[u].items += updates[u]

inspects = [m.inspected for m in monkeys]
s = sorted(inspects)
print(s[-2] * s[-1])









# TEST INPUT
# monkeys = [
#     Monkey([79, 98], '*', 19, 23, 2, 3),
#     Monkey([54, 65, 75, 74], '+', 6, 19, 2, 0),
#     Monkey([79, 60, 97], '**', 2, 13, 1, 3),
#     Monkey([74], '+', 3, 17, 0, 1)
# ]

# monkeys = [
#     Monkey([89, 73, 66, 57, 64, 80], '*', 3, 13, 6, 2),
#     Monkey([83, 78, 81, 55, 81, 59, 69], '+', 1, 3, 7, 4),
#     Monkey([76, 91, 58, 85], '*', 13, 7, 1, 4),
#     Monkey([71, 72, 74, 76, 68], '**', 2, 2, 6, 0),
#     Monkey([98, 85, 84], '+', 7, 19, 5, 7),
#     Monkey([78], '+', 8, 5, 3, 0),
#     Monkey([86, 70, 60, 88, 88, 78, 74, 83], '+', 4, 11, 1, 2),
#     Monkey([81, 58], '+', 5, 17, 3, 5)
# ]
