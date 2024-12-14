import re


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

def visualize_board(newNums):
    board = [['.' for _ in range(SAMPLE_WIDTH)] for _ in range(SAMPLE_HEIGHT)]
    for x, y, _, _ in newNums:
        board[y][x] = '#'

    for line in board:
        print("".join(line))

def overlap(nums):
    s = set()
    for x, y, _, _ in nums:
        if (x, y) in s:
            return True
        else:
            s.add((x, y))
    return False


for i in range(10000):
    newNums = []
    for x, y, vx, vy in nums:
        newx, newy = calculate_position(x, y, vx, vy, 1)
        newNums.append([newx, newy, vx, vy])
    nums = newNums
    if not overlap(nums):
        print("Iteration", i + 1)
        visualize_board(newNums)
