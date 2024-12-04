with open('./input.txt', 'r') as file:
    lines = file.readlines()

m = [list(line)[:-1] for line in lines]

result = 0
directions = [((0,0,0), (1,2,3)), ((1,2,3), (1,2,3)), ((1,2,3), (0,0,0)), ((1,2,3), (-1,-2,-3)),
              ((0,0,0), (-1,-2,-3)), ((-1,-2,-3), (-1,-2,-3)), ((-1,-2,-3), (0,0,0)), ((-1,-2,-3), (1,2,3))]
MAS = ["M", "A", "S"]

def countXmas(m, r, c):
    rows = len(m)
    cols = len(m[0])

    def checkIndex(d):
        finalRow = r + d[0][-1]
        finalCol = c + d[1][-1]
        return not (finalRow < 0 or finalRow >= rows or finalCol < 0 or finalCol >= cols)

    def checkDirection(d):
        if not checkIndex(d):
            return 0
        #import ipdb; ipdb.set_trace()
        for i in range(3):
            if m[r+d[0][i]][c+d[1][i]] != MAS[i]:
                return 0
        return 1

    return sum(checkDirection(d) for d in directions)


for r in range(len(m)):
    for c in range(len(m[0])):
        if m[r][c] == 'X':
            result += countXmas(m, r, c)

print(result)
