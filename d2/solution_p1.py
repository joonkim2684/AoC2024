with open('./input.txt', 'r') as file:
    lines = file.readlines()

result = 0
for line in lines:
    l = [int(x) for x in line.split()]

    increasing = True
    safe = True
    if l[0] == l[1]:
        safe = False
    elif l[0] > l[1]:
        increasing = False

    if increasing:
        for i in range(1, len(l)):
            if l[i-1] >= l[i] or l[i-1] + 3 < l[i]:
                safe = False

    else:
        for i in range(1, len(l)):
            if l[i-1] <= l[i] or l[i-1] - 3 > l[i]:
                safe = False

    if safe:
        result += 1
        print(l)

print(result)
