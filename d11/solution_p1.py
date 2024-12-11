with open('./input.txt', 'r') as file:
    lines = file.readlines()

stones = list(map(int, lines[0].split()))

START = 25 

queue = [(stone, START) for stone in stones]

def blink(currStone, blinksLeft):
    if currStone == 0:
        return [(1, blinksLeft - 1)]
    strStone = str(currStone)
    if len(strStone) % 2 == 0:
        return [(int(strStone[:len(strStone) // 2]), blinksLeft - 1), (int(strStone[len(strStone) // 2:]), blinksLeft - 1)]
    else:
        return [(currStone * 2024, blinksLeft - 1)]


result = 0
while queue:
    currStone, blinksLeft = queue.pop()
    if not blinksLeft:
        result += 1
    else:
        queue.extend(blink(currStone, blinksLeft))

print(result)
