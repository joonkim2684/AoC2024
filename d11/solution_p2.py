with open('./input.txt', 'r') as file:
    lines = file.readlines()

stones = list(map(int, lines[0].split()))

START = 75 

cache = {}

queue = [(stone, START) for stone in stones]

def getChild(currStone, blinksLeft):
    if currStone == 0:
        return [(1, blinksLeft - 1)]
    strStone = str(currStone)
    if len(strStone) % 2 == 0:
        return [(int(strStone[:len(strStone) // 2]), blinksLeft - 1), (int(strStone[len(strStone) // 2:]), blinksLeft - 1)]
    else:
        return [(currStone * 2024, blinksLeft - 1)]

def blink(currStone, blinksLeft):
    if blinksLeft == 0:
        return 1
    if (currStone, blinksLeft) in cache:
        return cache[(currStone, blinksLeft)]
    else:
        children = getChild(currStone, blinksLeft)
        result = 0
        for child in children:
            result += blink(*child)
        cache[(currStone, blinksLeft)] = result
        return result

result = sum(blink(stone, START) for stone in stones)
print(result)
