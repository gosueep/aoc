
file = open('lines.txt', 'r')
lines = file.readlines()



oxyLines = lines
i = 0
while(len(oxyLines) != 1) :

    numlist = [0] * (len(lines[0]) - 1)

    for string in oxyLines:
        string = string.strip()
        j = 0
        for num in string:
            num = int(num)
            numlist[j] += num
            j += 1

    gamma = ""

    for bit in numlist:
        if bit == (len(oxyLines) / 2):
            gamma += '*'
        elif bit > (len(oxyLines) / 2):
            gamma += '1'
        else:
            gamma += '0'


    templist = []
    for string in oxyLines:
        if(gamma[i] == '*' and (string.strip())[i] == '1' ):
            templist.append(string.strip())
        elif(gamma[i] == (string.strip())[i]):
            templist.append(string.strip())

    oxyLines = templist
    i += 1

print(oxyLines)
print(int(oxyLines[0], 2))

c02 = lines
i = 0
while(len(c02) != 1) :

    numlist = [0] * (len(lines[0]) - 1)

    for string in c02:
        string = string.strip()
        j = 0
        for num in string:
            num = int(num)
            numlist[j] += num
            j += 1

    epsilon = ""

    for bit in numlist:
        if bit == (len(c02) / 2):
            epsilon += '*'
        elif bit > (len(c02) / 2):
            epsilon += '0'
        else:
            epsilon += '1'

    templist = []
    for string in c02:
        if(epsilon[i] == '*' and (string.strip())[i] == '0'):
            templist.append(string.strip())
        elif(epsilon[i] == (string.strip())[i]):
            templist.append(string.strip())

    if(len(templist) != 0):
        c02 = templist
    i += 1

print(c02)
print(int(c02[0], 2))

print(int(oxyLines[0], 2) * int(c02[0], 2))

