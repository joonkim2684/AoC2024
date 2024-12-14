import re
import math

with open('./input.txt', 'r') as file:
    lines = file.readlines()

SAMPLE_HEIGHT = 103
SAMPLE_WIDTH = 101
ITERATIONS = 100

nums = []
for i in range(len(lines)):
    nums.append(list(map(int, re.findall(r'-*\d+', lines[i]))))

def calculate_position(x, y, vx, vy, ITERATIONS):
    newx = (x + vx * ITERATIONS) % SAMPLE_WIDTH
    newy = (y + vy * ITERATIONS) % SAMPLE_HEIGHT

    return newx, newy

def update_quadrant(quadrants, newx, newy):
    if newx in range(SAMPLE_WIDTH // 2):
        if newy in range(SAMPLE_HEIGHT // 2):
            quadrants[0] += 1
        elif newy in range(SAMPLE_HEIGHT // 2 + 1, SAMPLE_HEIGHT):
            quadrants[1] += 1
    elif newx in range(SAMPLE_WIDTH // 2 + 1, SAMPLE_WIDTH):
        if newy in range(SAMPLE_HEIGHT // 2):
            quadrants[2] += 1
        elif newy in range(SAMPLE_HEIGHT // 2 + 1, SAMPLE_HEIGHT):
            quadrants[3] += 1


quadrants = [0, 0, 0, 0]
for x, y, vx, vy in nums:
    newx, newy = calculate_position(x, y, vx, vy, ITERATIONS)
    update_quadrant(quadrants, newx, newy)

print(quadrants)
print(math.prod(quadrants))
