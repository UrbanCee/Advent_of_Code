with open("inputs/day02.txt") as fp:
    memory_init=[int(v) for v in fp.read().strip().split(",")]



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

def initialize(noun,verb):
    return [memory_init[0],noun,verb]+memory_init[3:]

print("Task1: ",run(initialize(12,2))[0])

for v in range(100):
    for n in range(100):
        if run(initialize(n,v))[0]==19690720:
            print("Task2: ",100*n+v)