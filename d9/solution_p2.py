with open('./input.txt', 'r') as file:
    lines = file.readlines()

input = list(map(int, list(lines[0])))

disk = [(i//2, x) if i % 2 == 0 else (-1, x) for i, x in enumerate(input)]


def attemptMove(disk, fileIndex):
    #import ipdb; ipdb.set_trace()
    file = disk.pop(fileIndex)
    assert file[0] != -1


    for i in range(0, fileIndex):
        space = disk[i]
        if space[0] != -1:
            continue
        
        if space[1] >= file[1]:
            _, emptySpace = disk.pop(i)
            disk.insert(fileIndex - 1, (-1, file[1]))
            leftoverSpace = emptySpace - file[1]
            if leftoverSpace > 0:
                disk.insert(i, (-1, leftoverSpace))
            disk.insert(i, file)
            return
    disk.insert(fileIndex, file)
            


def diskToList(disk):
    l = []
    for (value, repeat) in disk:
        l.extend([value for _ in range(repeat)])

    return l

maxId = len(disk) // 2
for id in range(maxId, 0, -1):
    fileIndex = [i for i, (value, _) in enumerate(disk) if value == id][0]
    attemptMove(disk, fileIndex)

result = 0
for i, value in enumerate(diskToList(disk)):
    if value == -1:
        continue
    result += i * value

print(result)
