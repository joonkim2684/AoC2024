with open('./input.txt', 'r') as file:
    lines = file.readlines()

def checkIncreasing(l, dampening):
    for i in range(1, len(l)):
        if l[i-1] >= l[i] or l[i-1] + 3 < l[i]:
            if dampening:
                l[i] = l[i-1]
                dampening = False
            else:
                return False
    return True

def checkDecreasing(l, dampening):
    for i in range(1, len(l)):
        if l[i-1] <= l[i] or l[i-1] - 3 > l[i]:
            if dampening:
                l[i] = l[i-1]
                dampening = False
            else:
                return False
    return True

s = 0
for line in lines:
    l = [int(x) for x in line.split()]

    if checkIncreasing(l[::1], True) or checkIncreasing(l[::-1], True) or checkDecreasing(l[::1], True) or checkDecreasing(l[::-1], True):
        s += 1

print(s)


