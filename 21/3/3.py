
file = open('lines.txt', 'r')
lines = file.readlines()

numlist = [0] * (len(lines[0]) -1)

print(numlist)

for string in lines:
    string = string.strip()
    i = 0
    for num in string:
        num = int(num)
        numlist[i] += num
        i += 1


print(numlist)

gamma = ""
epsilon = ""

for bit in numlist:
    if bit > (len(lines) / 2):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'


print('Gamma', gamma, ' = ', int(gamma) )
#935
print('Epsilon', epsilon, ' = ', int(epsilon))
#3160

print(935 * 3160)