with open('./sample_input.txt', 'r') as file:
    lines = file.readlines()

m = [list(line)[:-1] for line in lines]

result = 0
directions = [((-1,0,1), (-1,0,1)), ((-1,0,1), (1,0,-1)), ((1,0,-1), (1,0,-1)), ((1,0,-1), (-1,0,1))]
MAS = ["M", "A", "S"]

def countCrossmas(m, r, c):
    rows = len(m)
    cols = len(m[0])

    def checkIndex(d):
        startRow = r + d[0][0]
        finalRow = c + d[1][0]
        startCol = r + d[0][-1]
        finalCol = c + d[1][-1]
        return not (finalRow < 0 or finalRow >= rows or finalCol < 0 or finalCol >= cols
            or startRow < 0 or startRow >= rows or startCol < 0 or startCol >= cols)

    def checkDirection(d):
        if not checkIndex(d):
            return 0
        for i in range(3):
            if m[r+d[0][i]][c+d[1][i]] != MAS[i]:
                return 0
        return 1

    return sum(checkDirection(d) for d in directions)==2


for r in range(len(m)):
    for c in range(len(m[0])):
        if m[r][c] == 'A':
            result += countCrossmas(m, r, c)

print(result)
