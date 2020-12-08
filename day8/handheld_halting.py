with open('input.txt', 'r') as f:
    bytecode = tuple(f.readlines())

ac = 0
pc = 0

run_lines = set()

def start_exe(bytecode):
    while pc < len(bytecode):
        run_op(bytecode[pc])
        if pc in run_lines:
            return False
        run_lines.add(pc)
        #print(ac)
    return True


def run_op(inst):
    op, val = inst.split()
    #print(op, val)
    get_op(op)(val)

def get_op(op):

    return globals()[op]

def acc(x):
    global ac
    ac += int(x)
    inc_pc()

def jmp(x):
    global pc
    pc += int(x)

def nop(x):
    inc_pc()

def inc_pc():
    global pc
    pc += 1


def find_halt(bytecode):
    for i, val in enumerate(bytecode):
        global ac
        global pc
        global run_lines
        ac = 0
        pc = 0
        run_lines = set()
        if val[:3] == 'jmp':
            temp = list(bytecode)
            temp[i] = f'nop {val[4:]}'
            temp = tuple(temp)
            if start_exe(temp):
                return ac


print(find_halt(bytecode))