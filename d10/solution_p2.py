with open('./input.txt', 'r') as file:
    lines = file.readlines()

board = [list(map(int, list(line.replace('\n', '')))) for line in lines]

ans_board = [[1 if board[x][y] == 0 else 0 for y in range(len(board[0]))] for x in range(len(board))]


def printBoard(board):
    for i in range(len(board)):
        print(board[i])

def inBoard(board, x, y):
    return not (x < 0 or x >= len(board) or y < 0 or y >= len(board[0]))

def checkAdjacent(board, x, y, height):
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    result = 0
    for dx, dy in direction:
        if inBoard(board, x+dx, y+dy) and board[x+dx][y+dy] == height - 1:
            result += ans_board[x+dx][y+dy]
    return result

def fillHeight(board, ans_board, height):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == height:
                ans_board[x][y] = checkAdjacent(board, x, y, height)

for i in range(1, 10):
    fillHeight(board, ans_board, i)

result = 0
for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] == 9:
            result += ans_board[x][y]
print(result)
