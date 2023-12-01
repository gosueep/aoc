file = open('input.txt', 'r')
lines = file.readlines()

sum = 0
for line in lines:
    first, second = line[:len(line)//2], set(line[len(line)//2:])

    for f in first:
        if f in second:
            if f.islower():
                p = ord(f) - ord('a')
            else:
                p = ord(f) - ord('A') + 26
            print(p+1, f)
            sum += p+1
            break

print(sum)
