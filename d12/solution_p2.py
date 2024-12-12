with open('./input.txt', 'r') as file:
    lines = file.readlines()

board = [list(line.replace('\n', '')) for line in lines]

def inBoard(x, y):
    return not (x < 0 or x >= len(board) or y < 0 or y >= len(board[0]))

NEIGHBORS = set([(1, 0), (-1, 0), (0, 1), (0, -1)])

visited = []

def getOpenSides(x, y, c):
    openSides = []

    for dx, dy in NEIGHBORS:
        if not inBoard(x+dx, y+dy) or (board[x+dx][y+dy] != c):
            openSides.append((dx, dy))

    return set(openSides)

def checkDoubleEdgeCount(x, y, dx, dy, c, allOpenSides):
    if (dx, dy) in [(1, 0), (-1, 0)]:
        toCheck = [(0, 1), (0, -1)]
    else:
        toCheck = [(1, 0), (-1, 0)]

    result = 1
    for nx, ny in toCheck:
        if board[x][y] == c and (x+nx, y+ny) in allOpenSides and (dx, dy) in allOpenSides[(x+nx, y+ny)]:
            result -= 1
    return result

def searchNeighbors(x, y, c):
    global visited
    area, perimeter = 0, 0
    visited.append((x, y))


    openSides = getOpenSides(x, y, c)
    allOpenSides = {(x, y) : openSides}
    for dx, dy in NEIGHBORS - openSides:
        if (x+dx, y+dy) not in visited:
            searchedArea, searchedPerimeter, neighborOpenSides = searchNeighbors(x+dx, y+dy, c)        
            area += searchedArea
            perimeter += searchedPerimeter
            allOpenSides.update(neighborOpenSides)
    for dx, dy in openSides:
        perimeter +=  checkDoubleEdgeCount(x, y, dx, dy, c, allOpenSides)
    area += 1


    return area, perimeter, allOpenSides

result = 0

for x in range(len(board)):
    for y in range(len(board[0])):
        if (x, y) not in visited:
            area, perimeter, _ = searchNeighbors(x, y, board[x][y])
            result += area * perimeter
        
print(result)
