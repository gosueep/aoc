
file = open('1_lines.txt', 'r')
lines = file.readlines()

temp = int(lines[0])
count = 0

for i in range(0, len(lines) - 3):
    if(int(lines[i]) < int(lines[i+3])):
        count += 1

print(count)