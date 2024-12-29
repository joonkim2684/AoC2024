with open('./sample_input.txt', 'r') as file:
    lines = file.readlines()

def find_initial_register_value(line):
    return int(line.replace('\n', '').split(' ')[-1])

ra = -1
rb = find_initial_register_value(lines[1])
rc = find_initial_register_value(lines[2])

program = list(map(int, lines[4].split(' ')[-1].split(',')))


def run_with_registers(a, b, c):
    def fetch_combo_operand(operand) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c
            case _:
                assert False

    steps = 0
    pc = 0
    toMatch = 0
    output = []

    while pc <= len(program) - 1:
        opcode, operand = program[pc], program[pc+1]
        match opcode:
            case 0:
                denominator = 2 ** fetch_combo_operand(operand)
                a = a // denominator
                pc += 2
            case 1:
                b = b ^ operand
                pc += 2
            case 2:
                b = fetch_combo_operand(operand) % 8
                pc += 2
            case 3:
                if a == 0:
                    pc += 2
                else:
                    pc = operand
            case 4:
                b = b ^ c
                pc += 2
            case 5:
                output.append(fetch_combo_operand(operand) % 8)
                if toMatch == len(program) - 1:
                    break
                if fetch_combo_operand(operand) % 8 != program[toMatch]:
                    break
                else:
                    toMatch += 1
                pc += 2
            case 6:
                denominator = 2 ** fetch_combo_operand(operand)
                b = a // denominator
                pc += 2
            case 7:
                denominator = 2 ** fetch_combo_operand(operand)
                c = a // denominator
                pc += 2
        steps += 1
        if steps > 1000:
            break
    return output

for a in range(10000000, 100000000):
    if a % 1000 == 0:
        print(f"currently at a = {a}")
    if program == run_with_registers(a, rb, rc):
        print(a)
        break
