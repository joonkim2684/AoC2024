with open('./input.txt', 'r') as file:
    lines = file.readlines()

board = [list(line.replace('\n', '')) for line in lines]

def inBoard(board, x, y):
    return not (x < 0 or x >= len(board) or y < 0 or y >= len(board[0]))

NEIGHBORS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = []
print(board[9][8])
def searchNeighbors(board, x, y, c):
    global visited
    area, perimeter = 0, 0
    visited.append((x, y))

    for dx, dy in NEIGHBORS:
        inB = inBoard(board, x+dx, y+dy)
        if inB and (board[x+dx][y+dy] == c):
            if (x+dx, y+dy) not in visited:
                searchedArea, searchedPerimeter = searchNeighbors(board, x+dx, y+dy, c)        
                area += searchedArea
                perimeter += searchedPerimeter
        else:
            perimeter += 1
    area += 1

    return area, perimeter

result = 0

for x in range(len(board)):
    for y in range(len(board[0])):
        if (x, y) not in visited:
            area, perimeter = searchNeighbors(board, x, y, board[x][y])
            result += area * perimeter
        
print(result)
