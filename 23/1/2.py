import sys
import re

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()

d = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

out = 0
for i in lines:
    curr = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|\d))', i)
    
    l = curr[0]
    if l.isalpha():l = d[l]
    r = curr[-1]
    if r.isalpha():r = d[r] 
    
    out += int(l+r)
    
print(out)