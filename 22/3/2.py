file = open('input.txt', 'r')
lines = file.readlines()

sum = 0
for idx in range(0, len(lines), 3):

    one = set(lines[idx].strip())
    two = set(lines[idx+1].strip())
    three = set(lines[idx+2].strip())

    print(lines[idx].strip(), lines[idx+1].strip(), lines[idx+2].strip())

    elves = [one, two, three]
    lens = [len(e) for e in elves]
    i = lens.index(max(lens))

    biggest = elves[i]
    # print(lens)
    # print(i)
    # print(biggest)

    for f in biggest:
        if f in one and f in two and f in three:
            if f.islower():
                p = ord(f) - ord('a')
            else:
                p = ord(f) - ord('A') + 26
            sum += p+1
            break

print(sum)
