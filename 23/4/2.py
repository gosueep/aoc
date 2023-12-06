import sys

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()
N = len(lines)
amt = [1 for _ in range(N+1)]
amt[0] = 0

total = 0
for line in lines:
    card = line.split()
    winning = set(map(int, card[2:card.index('|')]))
    nums = list(map(int, card[card.index('|')+1:]))
    
    count = 0
    for i in nums:
        if i in winning: count += 1
    
    orig = int(card[1][:-1])
    for i in range(orig+1, min(orig+count+1, N+1)):
        amt[i] += amt[orig]
print(sum(amt))