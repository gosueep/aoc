
file = open('lines.txt', 'r')
lines = file.readlines()

x = 0
aim = 0
depth = 0

for i in lines:
    line = i.split()

    if(line[0] == 'forward'):
        x += int(line[1])
        depth += (aim * int(line[1]))

    elif (line[0] == 'up'):
        aim -= int(line[1])

    elif (line[0] == 'down'):
        aim += int(line[1])


print('X:', x)
print('Aim', aim)
print('Depth:', depth)
print(x * depth)