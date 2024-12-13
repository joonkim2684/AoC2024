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
b_plus = 10000000000000

for i in range(len(l1)):
    b = np.array(list(map(int, bl[i]))) + np.array([b_plus, b_plus])
    A = np.array([list(map(int, l1[i])), list(map(int, l2[i]))]).T
    constraints = LinearConstraint(A, b, b)
    res = milp(c=c, constraints=constraints)
    is_integral = res.x is not None and all(np.abs(np.round(list(res.x)) - list(res.x)) < 1e-3)
    if is_integral:
        result += res.fun

print(result)
