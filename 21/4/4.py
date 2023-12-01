
file = open('lines.txt', 'r')
lines = file.readlines()


order = []
firstLine = lines[0].split(",")

for num in firstLine:
    order.append(int(num))

print(order)



boards = []

for i in range(2, len(lines), 6):

    board = []

    for j in range(0,5):
        line = lines[i+j].split()
        boardLine = []
        for num in line:
            boardLine.append(int(num.strip()))

        board.append(boardLine)

    boards.append(board)

print(boards)


def check(board, draw):
    for b in range(0, len(boards)):

        for line in range(0,len(board)):
            for number in range(0,len()):

                if board[b][line][number] == draw:

                    #check horizontal
                    Win = True
                    score = 0
                    for horizontalNum in board[b][line]:
                        score += horizontalNum
                        if horizontalNum in checked:
                            Win = False
                            break

                    if(Win):
                        return score

                    #check vertical
                    for verticalNum in range(0, 5):
                        if


checked = []
for draw in order:
    checked.append(draw)

    for b in range(0, len(boards)):
        check(boards[b], draw)
