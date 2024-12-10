with open('./input.txt', 'r') as file:
    lines = file.readlines()

board = [list(map(int, list(line.replace('\n', '')))) for line in lines]

ans_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]


def printBoard(board):
    for i in range(len(board)):
        print(board[i])

def inBoard(board, x, y):
    return not (x < 0 or x >= len(board) or y < 0 or y >= len(board[0]))

def findAdjacentStep(board, x, y, height):
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    result = []
    for dx, dy in direction:
        if inBoard(board, x+dx, y+dy) and board[x+dx][y+dy] == height - 1:
            result.append((x+dx, y+dy, height-1))
    return result

def searchZeros(board, x, y):
    result = 0
    visited = set()
    queue = [(x, y, 9)]
    while queue:
        currX, currY, currH = queue.pop()
        if (currX, currY) not in visited:
            if currH == 0:
                result += 1
            visited.add((currX, currY))
            steps = findAdjacentStep(board, currX, currY, currH)
            queue.extend(steps)
    return result

result = 0
for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] == 9:
            result += searchZeros(board, x, y)

print(result)
