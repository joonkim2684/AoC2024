with open('./input.txt', 'r') as file:
    lines = file.readlines()

def search_tree(curr, goal, operands):
    if curr == goal and not operands:
        return True
    if not operands or curr > goal:
        return False
    else:
        return search_tree(curr * operands[0], goal, operands[1:]) or search_tree(curr + operands[0], goal, operands[1:])

goal_list = []
operands_list = []
for line in lines:
    line = line.split(" ")
    goal_list.append(int(line[0][:-1]))
    operands_list.append([int(x) for x in line[1:]])

result = 0
for goal, operands in zip(goal_list, operands_list):
    if search_tree(operands[0], goal, operands[1:]):
        result += goal

print(result)
