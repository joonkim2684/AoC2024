from queue import PriorityQueue

with open('./input.txt', 'r') as file:
    lines = file.readlines()

board = list(map(lambda x: x.replace('\n', ''), lines))

def printBoard(board):
    for i in range(len(board)):
        print(''.join(board[i]))

def vectorDiff(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

def vectorAdd(p1, p2):
    return (p2[0] + p1[0], p2[1] + p1[1])

def getElementInPosition(p):
    return board[p[0]][p[1]]

# printBoard(board)

q = PriorityQueue()

start_position = (len(board) - 2, 1)
start_velocity = (0, 1)
start_state = (start_position, start_velocity)

cache = {start_state: 0}
q.put((0, start_state))

while q:
    score, (position, velocity) = q.get()

    if getElementInPosition(position) == 'E':
        print(score)
        break
    
    newPosition = vectorAdd(position, velocity)
    if getElementInPosition(newPosition) != '#':
        newState = (newPosition, velocity)
        if newState not in cache or cache[newState] > score + 1:
            q.put((score + 1, newState))
            cache[newState] = score + 1

    cwVelocity = (velocity[1], -velocity[0])
    ccwVelocity = (-velocity[1], velocity[0])

    for newVelocity in [cwVelocity, ccwVelocity]:
        newState = (position, newVelocity)
        if newState not in cache or cache[newState] > score + 1000:
            q.put((score + 1000, newState))
            cache[newState] = score + 1000

