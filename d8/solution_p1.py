with open('./input.txt', 'r') as file:
    lines = file.readlines()

board = [list(line.replace('\n', '')) for line in lines]

coordinate_dict = {}

for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] != '.':
            if board[x][y] not in coordinate_dict:
                coordinate_dict[board[x][y]] = [(x, y)]
            else:
                coordinate_dict[board[x][y]].append((x, y))

def inBoard(board, position):
    return not (position[0] < 0 or position[0] >= len(board) or position[1] < 0 or position[1] >= len(board[0]))

import itertools
pairs = []
for value in coordinate_dict.values():
    pairs += (list(itertools.combinations(value, 2)))

def vectorDiff(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

def vectorAdd(p1, p2):
    return (p2[0] + p1[0], p2[1] + p1[1])

def getAntinodes(p1, p2):
    diff = vectorDiff(p1, p2)
    anti1 = vectorDiff(diff, p1)
    anti2 = vectorAdd(p2, diff)

    return [x for x in [anti1, anti2] if inBoard(board, x)]

resultSet = set()
for pair in pairs:
    resultSet.update(getAntinodes(pair[0], pair[1]))

print(len(resultSet))
