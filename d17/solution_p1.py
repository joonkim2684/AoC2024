with open('./input.txt', 'r') as file:
    lines = file.readlines()

def find_initial_register_value(line):
    return int(line.replace('\n', '').split(' ')[-1])

ra = find_initial_register_value(lines[0])
rb = find_initial_register_value(lines[1])
rc = find_initial_register_value(lines[2])
pc = 0

program = list(map(int, lines[4].split(' ')[-1].split(',')))
output = []

print(ra, rb, rc, program)

def fetch_combo_operand(operand) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return ra
        case 5:
            return rb
        case 6:
            return rc
        case _:
            assert False

def repl(opcode, operand):
    global ra, rb, rc, pc

    match opcode:
        case 0:
            denominator = 2 ** fetch_combo_operand(operand)
            ra = ra // denominator
            pc += 2
        case 1:
            rb = rb ^ operand
            pc += 2
        case 2:
            rb = fetch_combo_operand(operand) % 8
            pc += 2
        case 3:
            if ra == 0:
                pc += 2
            else:
                pc = operand
        case 4:
            rb = rb ^ rc
            pc += 2
        case 5:
            output.append(fetch_combo_operand(operand) % 8)
            pc += 2
        case 6:
            denominator = 2 ** fetch_combo_operand(operand)
            rb = ra // denominator
            pc += 2
        case 7:
            denominator = 2 ** fetch_combo_operand(operand)
            rc = ra // denominator
            pc += 2

while pc <= len(program) - 1:
    # print(f'ra: {ra}, rb: {rb}, rc: {rc}, pc: {pc} \nopcode: {program[pc]}, operand: {program[pc+1]}, combo: {fetch_combo_operand(program[pc+1])}')
    repl(program[pc], program[pc+1])

print(','.join(str(i) for i in output))
