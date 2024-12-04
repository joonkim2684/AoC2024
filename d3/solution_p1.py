import re

with open('./input.txt', 'r') as file:
    lines = file.readlines()

def mul(x, y):
    return x * y

result = 0
enabled = True
for line in lines:
    l = re.findall(r"mul\(\d+,\d+\)", line)
    for inst in l:
        result += eval(inst)

print(result)
