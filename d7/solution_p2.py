with open('./input.txt', 'r') as file:
    lines = file.readlines()

def pipe_op(x, y):
    return int(str(x) + str(y))


def search_tree(curr, goal, operands):
    if curr == goal and len(operands) == 0:
        return True
    elif len(operands) == 0 or curr > goal:
        return False
    else:
        return search_tree(pipe_op(curr, operands[0]), goal, operands[1:]) \
            or search_tree(curr * operands[0], goal, operands[1:]) \
            or search_tree(curr + operands[0], goal, operands[1:])

goal_list = []
operands_list = []
for line in lines:
    line = line.split(" ")
    goal_list.append(int(line[0][:-1]))
    operands_list.append([int(x) for x in line[1:]])

result = 0
count = 0
for goal, operands in zip(goal_list, operands_list):
    if search_tree(operands[0], goal, operands[1:]):
        result += goal
        count += 1

print(result)
