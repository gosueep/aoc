from collections import defaultdict
import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

conv = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


hands = []
for line in lines:
    hand, bid = line.split()
    bid = int(bid)
    
    t = []
    counts = defaultdict(int)
    for c in hand:
        t.append(conv[c])
        counts[conv[c]] +=1
    
    # print(sorted(counts.values(), reverse=True))
    # nums = sorted(counts.values(), reverse=True)
    pairs = list(counts.items())
    pairs.sort(key= lambda x: x[1], reverse=True)
    print(pairs)
    val = 0
    if pairs[0][1] == 5:
        val = 6
        t = pairs[0][0]
    elif pairs[0][1] == 4:
        val = 5
        t = (pairs[0][0], pairs[1][0])
    elif pairs[0][1] == 3:
        if pairs[1][1] == 2:
            val = 4
            t = (pairs[0][0], pairs[1][0])
        else:
            val = 3
            # t = (pairs[0][0], pairs[1][0], pairs[2][0])
            t = [pairs[1][0]] + sorted([x[0] for x in pairs[1:]], reverse=True)
    elif pairs[0][1] == 2:
        if pairs[1][1] == 2:
            val = 2
            # t = (pairs[0][0], pairs[1][0], pairs[2][0])
            t = sorted([x[0] for x in pairs[:2]], reverse=True) + [pairs[2][0]]
            print(t)
        else:
            val = 1
            # t = (pairs[0][0], pairs[1][0], pairs[2][0], pairs[3][0])
            t = [pairs[0][0]] + sorted([x[0] for x in pairs[1:]], reverse=True)
    # print(t)
    hands.append(((val, t), bid, hand))
    # print(hands[-1])
    
hands.sort(key = lambda x: x[0])
print(hands)

total = 0
for i in range(len(hands)):
    total += (i+1)* hands[i][1]
print(total)