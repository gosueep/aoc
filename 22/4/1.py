file = open('input.txt', 'r')
lines = file.readlines()

count = 0
for line in lines:
    l, r = line.strip().split(',')

    l_i, l_f = map(int, l.split('-'))
    r_i, r_f = map(int, r.split('-'))

    if l_i <= r_i and l_f >= r_f:
        count += 1
    elif r_i <= l_i and r_f >= l_f:
        count += 1

    print(l, r)
    print(l_i, l_f, r_i, r_f, count)

print(count)
