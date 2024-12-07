with open('./input.txt', 'r') as file:
    lines = file.readlines()

board = [list(line.replace('\n', '')) for line in lines]

def findGuard(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == '^':
                return (x, y)
    return (0, 0)

def inBoard(board, position):
    return not (position[0] < 0 or position[0] >= len(board) or position[1] < 0 or position[1] >= len(board[0]))

def rotateRight(velocity):
    return (velocity[1], -velocity[0])

def step(board, position, velocity):
    forwardPosition = [sum(x) for x in zip(position, velocity)]

    if not inBoard(board, forwardPosition):
        return tuple(forwardPosition), tuple(velocity)

    if board[forwardPosition[0]][forwardPosition[1]] == '#':
        nextVelocity = rotateRight(velocity)
        nextPosition = [sum(x) for x in zip(position, nextVelocity)]
        if board[nextPosition[0]][nextPosition[1]] == '#':
            return tuple(position), tuple(nextVelocity)
        else:
            return tuple(nextPosition), tuple(nextVelocity)
    else:
        return tuple(forwardPosition), tuple(velocity)


position = findGuard(board)
velocity = (-1, 0)

def isLooping(board, position, velocity):
    visited = set()

    while(inBoard(board, position)):
        if (position, velocity) in visited:
            return 1

        visited.add((position, velocity))
        position, velocity = step(board, position, velocity)
    return 0

def findPath(board, position, velocity):
    while(inBoard(board, position)):
        board[position[0]][position[1]] = 'X'
        position, velocity = step(board, position, velocity)
    return board

newBoard = findPath(board, position, velocity)

result = 0

board = newBoard
board[position[0]][position[1]] = '^'

for x in range(len(board)):
    print(f"on line {x}") if x%10 == 0 else ""
    for y in range(len(board[0])):
        if board[x][y] == 'X':
            board[x][y] = '#'
            result += isLooping(board, position, velocity)
            board[x][y] = 'X'

print(result)
