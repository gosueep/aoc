import sys
import copy

FILENAME = 'input.txt'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    FILENAME = 'test.txt'

file = open(FILENAME, 'r')
lines = file.readlines()


class rock:
    def __init__(self, type, floor):

        h = floor + 4
        self.h = h

        if type == 0:
            self.positions = [
                (3, h), (4, h), (5, h), (6, h)
            ]
        elif type == 1:
            self.positions = [
                            (4, h+2),
                (3, h+1), (4, h+1), (5, h+1),
                            (4, h)
            ]
            self.h += 2
        elif type == 2:
            self.positions = [
                                (5, h+2),
                                (5, h+1),
                (3, h), (4, h), (5, h)
            ]
            self.h += 2
        elif type == 3:
            self.positions = [
                (3, h+3),
                (3, h+2),
                (3, h+1),
                (3, h),
            ]
            self.h += 3
        elif type == 4:
            self.positions = [
                (3, h+1), (4, h+1),
                (3, h), (4, h)
            ]
            self.h += 1

    def push(self, direction):
        delta = 1 if direction == '>' else -1
        new_positions = []
        for x, y in self.positions:
            new_x = x+delta
            if 1 > new_x or new_x > 7 or (new_x, y) in cave:            # unable to push
                return False
            new_positions.append((new_x, y))
        self.positions = new_positions

    def fall(self):
        new_positions = []
        for x, y in self.positions:
            new_pos = (x, y-1)
            if new_pos in cave or y < 0:              # unable to fall
                for p in self.positions:
                    cave.add(p)
                return self.h
            new_positions.append(new_pos)
        self.positions = new_positions
        self.h -= 1
        return -1


width = 7       # walls at (0, y), (8, 0)
high = 0       # floor at (x, 0)
cave = set([(x, 0) for x in range(0, 9)])

dirs = lines[0]
rocknum = 0
d = 0
fout = open('my.txt', 'w')
while rocknum < 2024:

    r = rock(rocknum % 5, high)

    falling = -1
    while falling == -1:
        r.push(dirs[d])
        d = (d+1) % len(dirs)
        falling = r.fall()

    if falling > high:
        high = falling

    print(high)
    fout.write(f'{high}\n')
    # actual = max([p[1] for p in cave])
    # if high != actual:
    #     print(rocknum+1, '-', high, actual)

    rocknum += 1

actual = max([p[1] for p in cave])
print(high, actual)









