with open('./input.txt', 'r') as file:
    lines = file.readlines()

input = map(int, list(lines[0]))

disk = []
id = 0
for i, value in enumerate(input):
    if i % 2 == 0:
        for _ in range(value):
            disk.append(id)
        id += 1
    else:
        for _ in range(value):
            disk.append(-1)

def findNextSpace(disk, spacePointer):
    for i in range(spacePointer, len(disk)):
        if disk[i] == -1:
            return i
    return -1

def findPrevFile(disk, filePointer):
    for i in range(filePointer, 0, -1):
        if disk[i] != -1:
            return i
    return -1

spacePointer = findNextSpace(disk, 0)
filePointer = findPrevFile(disk, len(disk) - 1)

while spacePointer < filePointer:
    disk[spacePointer] = disk[filePointer]
    disk[filePointer] = -1

    spacePointer = findNextSpace(disk, spacePointer)
    filePointer = findPrevFile(disk, filePointer)

result = 0
for i, value in enumerate(disk):
    if value == -1:
        break
    result += i * value

print(result)
