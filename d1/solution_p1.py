with open('./input.txt', 'r') as file:
    lines = file.readlines()

l1, l2 = [], []

for line in lines:
    n1, n2 = line.split()
    l1.append(int(n1))
    l2.append(int(n2))

l1.sort()
l2.sort()

result = 0

for x, y in zip(l1, l2):
    result += abs(x - y)

print(result)
