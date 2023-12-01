file = open('input.txt', 'r')
lines = file.readlines()

count = 0
for line in lines:
    l, r = line.strip().split(',')

    l_i, l_f = map(int, l.split('-'))
    r_i, r_f = map(int, r.split('-'))

    l = range(l_i, l_f + 1)
    r = range(r_i, r_f + 1)

    for num in l:
        if num in r:
            count += 1
            break

print(count)
