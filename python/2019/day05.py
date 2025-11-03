with open("inputs/day05.txt") as fp:
    memory_init = [int(r) for r in fp.read().strip().split(",")]

def run(memory):
    pc = 0
    while pc<len(memory):
        opcode = memory[pc]
        if (opcode == 99):
            break
        if (opcode == 1):
            memory[memory[pc+3]]=memory[memory[pc+1]]+memory[memory[pc+2]]
        if (opcode == 2):
            memory[memory[pc+3]]=memory[memory[pc+1]]*memory[memory[pc+2]]

        pc+=4
    return memory
