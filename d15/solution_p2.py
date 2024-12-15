with open('./input.txt', 'r') as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace('\n', '').replace('.', '..').replace('@', '@.').replace('O', '[]').replace('#', '##'), lines))

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

def findBoxPairPosition(boxPosition):
    boxElement = getElementInPosition(boxPosition)
    if boxElement == '[':
        return vectorAdd(boxPosition, (0, 1))
    elif boxElement == ']':
        return vectorAdd(boxPosition, (0, -1))

    assert False


def moveToEmptyPosition(front):
    global position
    setElementInPosition(position, '.')
    setElementInPosition(front, '@')
    position = front

def moveElementToEmptyPosition(position, direction):
    assert getElementInPosition(vectorAdd(position, direction)) == '.'
    element = getElementInPosition(position)
    setElementInPosition(position, '.')
    setElementInPosition(vectorAdd(position, direction), element)
    
def findEmptySpace(direction, front):
    while getElementInPosition(front) in ['[', ']']:
        front = vectorAdd(front, direction)
    if getElementInPosition(front) == '#':
        return None
    elif getElementInPosition(front) == '.':
        return front

def canPushBox(bp1, bp2, direction):
    bp1_next, bp2_next = vectorAdd(bp1, direction), vectorAdd(bp2, direction)
    bp1_next_elem, bp2_next_elem = getElementInPosition(bp1_next), getElementInPosition(bp2_next)
    if bp1_next_elem == '#' or bp2_next_elem == '#':
        return False

    possible = True
    if bp1_next_elem in ['[', ']']:
        possible &= canPushBox(bp1_next, findBoxPairPosition(bp1_next), direction)
    if bp2_next_elem in ['[', ']']:
        possible &= canPushBox(bp2_next, findBoxPairPosition(bp2_next), direction)
    return possible

def pushBox(bp1, bp2, direction):
    bp1_next, bp2_next = vectorAdd(bp1, direction), vectorAdd(bp2, direction)
    bp1_next_elem = getElementInPosition(bp1_next)
    if bp1_next_elem in ['[', ']']:
        pushBox(bp1_next, findBoxPairPosition(bp1_next), direction)

    bp2_next_elem = getElementInPosition(bp2_next)
    if bp2_next_elem in ['[', ']']:
        pushBox(bp2_next, findBoxPairPosition(bp2_next), direction)

    moveElementToEmptyPosition(bp1, direction)
    moveElementToEmptyPosition(bp2, direction)

def attemptPush(direction, front):
    if direction in [(0, 1), (0, -1)]:
        if emptySpace := findEmptySpace(direction, front):
            while emptySpace != front:
                emptySpace = vectorDiff(direction, emptySpace)
                moveElementToEmptyPosition(emptySpace, direction)
            moveToEmptyPosition(front)
    else: # attempting push up or down
        boxPair = findBoxPairPosition(front)
        if canPushBox(front, boxPair, direction):
            pushBox(front, boxPair, direction)
            moveToEmptyPosition(front)

def attemptMove(direction):
    front = vectorAdd(position, direction)
    frontElement = getElementInPosition(front)
    if frontElement == '.':
        moveToEmptyPosition(front)
    elif frontElement == '[' or frontElement == ']':
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
        if board[x][y] == '[':
            result += 100*x + y

print(result)
