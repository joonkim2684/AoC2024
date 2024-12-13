import numpy as np
import re
from scipy.optimize import LinearConstraint
from scipy.optimize import milp

with open('./input.txt', 'r') as file:
    lines = file.readlines()

l1, l2, bl = [], [], []

for i in range(0, len(lines), 4):
    l1.append(re.findall(r'\d+', lines[i]))
    l2.append(re.findall(r'\d+', lines[i+1]))
    bl.append(re.findall(r'\d+', lines[i+2]))


c = np.array([3, 1])
integrality = np.ones_like(c)

result = 0
for i in range(len(l1)):
    b = np.array(bl[i])
    A = np.array([l1[i], l2[i]]).T
    constraints = LinearConstraint(A, b, b)
    res = milp(c=c, constraints=constraints, integrality=integrality)
    if res.fun:
        result += res.fun

print(result)
