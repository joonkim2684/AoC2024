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
        return forwardPosition, velocity

    if board[forwardPosition[0]][forwardPosition[1]] == '#':
        nextVelocity = rotateRight(velocity)
        nextPosition = [sum(x) for x in zip(position, nextVelocity)]
        return nextPosition, nextVelocity
    else:
        return forwardPosition, velocity
        
def countX(board):
    result = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 'X':
                result += 1
    return result


position = findGuard(board)
velocity = (-1, 0)


while(inBoard(board, position)):
    board[position[0]][position[1]] = 'X'
    position, velocity = step(board, position, velocity)

#for line in board:
#    print(line)
print(countX(board))
    
