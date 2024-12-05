with open('./input.txt', 'r') as file:
    lines = file.readlines()

def parsel1(s):
    x, y = s.replace('\n', '').split('|')
    return (int(x), int(y))

def parsel2(s):
    return [int(x) for x in s.split(',')]

l1, l2 = [], []
i = 0
while lines[i] != '\n':
    l1.append(parsel1(lines[i]))
    i += 1

for j in range(i+1, len(lines)):
    l2.append(parsel2(lines[j]))

result = 0
for line in l2:
    valid = 1
    for n1, n2 in l1:
        if n1 in line and n2 in line and line.index(n1) > line.index(n2):
            valid = 0
            break
    result += valid * line[len(line)//2]

print(result)
