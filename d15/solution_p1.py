with open('./input.txt', 'r') as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace('\n', ''), lines))

board = list(map(list, lines[:lines.index('')]))
instructions = ''.join(lines[lines.index('') + 1:])

def printBoard(board):
    for i in range(len(board)):
        print(''.join(board[i]))

print(instructions)
printBoard(board)

DIRECTION = {'>': (0, 1),
             '<': (0, -1),
             '^': (-1, 0),
             'v': (1, 0)}

position = None
for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] == '@':
            position = (x, y)
            break


def vectorDiff(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

def vectorAdd(p1, p2):
    return (p2[0] + p1[0], p2[1] + p1[1])

def getElementInPosition(p):
    return board[p[0]][p[1]]

def setElementInPosition(p, e):
    board[p[0]][p[1]] = e

def moveToEmptyPosition(front):
    global position
    setElementInPosition(position, '.')
    setElementInPosition(front, '@')
    position = front
    
def findEmptySpace(direction, front):
    while (getElementInPosition(front)) == 'O':
        front = vectorAdd(front, direction)
    if getElementInPosition(front) == '#':
        return None
    elif getElementInPosition(front) == '.':
        return front

def attemptPush(direction, front):
    if emptySpace := findEmptySpace(direction, front):
        setElementInPosition(emptySpace, 'O')
        moveToEmptyPosition(front)


def attemptMove(direction):
    front = vectorAdd(position, direction)
    frontElement = getElementInPosition(front)
    if frontElement == '.':
        moveToEmptyPosition(front)
    elif frontElement == 'O':
        attemptPush(direction, front)
    elif frontElement == '#':
        return


for move in list(instructions):
    direction = DIRECTION[move]
    attemptMove(direction)

printBoard(board)

result = 0
for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] == 'O':
            result += 100*x + y

print(result)
