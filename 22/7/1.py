from collections import defaultdict

file = open('input.txt', 'r')
lines = file.readlines()


sum = 0
total = 0
size = {}
subs = {}
currSum = 0
subdirs = []
for line in reversed(lines):
    l = line.split()

    if l[0].isnumeric():
        currSum += int(l[0])

    elif l[0] == 'dir':
        currSum += size[l[1]]
        subdirs.append([l[1]])

    elif l[1] == 'cd' and l[2] != '..':
        if currSum <= 100000:
            total += currSum
        size[l[2]] = currSum
        subs[l[2]] = subdirs
        currSum = 0
        subdirs = []

print(total)
