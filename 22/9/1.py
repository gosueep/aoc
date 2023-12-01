file = open('input.txt', 'r')
lines = file.readlines()

h = 5
w = 6

head = [4, 0]
tail = [4, 0]

visited = set()


def move():
    moveT()
    visited.add(tuple(tail))
    # print(head, tail)

def moveT_vert():
    if head[0] > tail[0]:
        tail[0] += 1
    else:
        tail[0] -= 1

def moveT_hor():
    if head[1] > tail[1]:
        tail[1] += 1
    else:
        tail[1] -= 1


def moveT():
    vert = head[0] - tail[0]
    hor = head[1] - tail[1]

    if abs(vert) > 1:
        if hor != 0:
            moveT_hor()
        moveT_vert()


    if abs(hor) > 1:
        if vert != 0:
            moveT_vert()
        moveT_hor()



for line in lines:
    # print(head, tail)
    # print()

    visited.add(tuple(tail))
    d, amt = line.split()
    amt = int(amt)


    for _ in range(amt):
        if d == 'L':
            head[1] -= 1
        elif d == 'R':
            head[1] += 1
        elif d == 'U':
            head[0] -= 1
        elif d == 'D':
            head[0] += 1

        move()
    #     print(head, tail)
    #
    # print(visited)
    # print(len(visited))



print(visited)
print(len(visited))