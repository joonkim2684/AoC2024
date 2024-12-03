with open('./input.txt', 'r') as file:
    lines = file.readlines()

l1 = []
d2 = {}

for line in lines:
    n1, n2 = line.split()
    l1.append(int(n1))
    n2 = int(n2)
    if n2 not in d2:
        d2[n2] = 0
    d2[n2] += 1

result = 0

for x in l1:
    if x in d2:
        result += x * d2[x]        

print(result)
