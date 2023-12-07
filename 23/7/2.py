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
    'J': 0,
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

    pairs = list(counts.items())
    pairs.sort(key= lambda x: x[1], reverse=True)
        
    newpairs = []
    added = False
    if conv['J'] in counts and len(counts) > 1:
        for card, num in pairs:
            if card != conv['J']:
                if not added:
                    newpairs.append((card, num + counts[conv['J']]))
                    added =True
                else:
                    newpairs.append((card, num))
        pairs = newpairs
    
    val = 0
    if pairs[0][1] == 5:
        val = 6
    elif pairs[0][1] == 4:
        val = 5
    elif pairs[0][1] == 3:
        if pairs[1][1] == 2:
            val = 4
        else:
            val = 3
    elif pairs[0][1] == 2:
        if pairs[1][1] == 2:
            val = 2
        else:
            val = 1
    t = [conv[x] for x in hand]
    hands.append(((val, t), bid, hand))
    
hands.sort(key = lambda x: x[0])
# print(hands)

total = 0
for i in range(len(hands)):
    total += (i+1)* hands[i][1]
print(total)