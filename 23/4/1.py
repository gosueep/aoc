import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

total = 0
for line in lines:
    card = line.split()
    winning = set(map(int, card[2:card.index('|')]))
    nums = list(map(int, card[card.index('|')+1:]))
    
    count = 0
    for i in nums:
        if i in winning: count += 1
    
    if count > 0:
        total += 2**(count-1)
    print(winning, nums)
print(total)