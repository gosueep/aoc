file = open('input.txt', 'r')
lines = file.readlines()

ROPE_LENGTH = 10
rope = [[0, 0] for x in range(ROPE_LENGTH)]
visited = {(0, 0)}


def moveT(head, tail, axis):       # Vert = rows = 0, Hor = cols = 1
    tail[axis] += (1 if head[axis] > tail[axis] else -1)

def move(head, tail):
    vert = head[0] - tail[0]
    hor = head[1] - tail[1]
    if abs(vert) > 1:
        if hor != 0:
            moveT(head, tail, 1)
        moveT(head, tail, 0)

    vert = head[0] - tail[0]
    hor = head[1] - tail[1]
    if abs(hor) > 1:
        if vert != 0:
            moveT(head, tail, 0)
        moveT(head, tail, 1)


for line in lines:
    head = rope[-1]
    tail = rope[0]

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

        for i in range(ROPE_LENGTH-1, 0, -1):
            move(rope[i], rope[i-1])
        visited.add(tuple(tail))

print(len(visited)) # 2427

