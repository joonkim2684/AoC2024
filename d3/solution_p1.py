import re

with open('./input.txt', 'r') as file:
    lines = file.readlines()

def mul(x, y):
    return x * y

result = 0
enabled = True
for line in lines:
    l = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line)
    print(l)
    for inst in l:
        if inst == "don't()":
            enabled = False
        elif inst == "do()":
            enabled = True
        elif enabled:
            result += eval(inst)

print(result)
