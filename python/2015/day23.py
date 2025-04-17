import re

insRex = "(hlf|tpl|inc|jmp|jie|jio) (a|b)*[, ]*\\+?([-]*\\d+)*"

program = []

with open("inputs/day23.txt") as fp:
    for line in fp.readlines():
        program += [(ins,reg,offset) for ins,reg,offset in re.findall(insRex,line)]

def run(a,b):
    pc=0
    regs = {"a":a, "b":b}
    while(pc<len(program)):
        ins,r,offset = program[pc]
        pc+=1
        if ins == "hlf":
            regs[r]=regs[r]//2
        elif ins == "tpl":
            regs[r]=regs[r]*3
        elif ins == "inc":
            regs[r]=regs[r]+1
        elif ins == "jmp":
            pc+=int(offset)-1
        elif ins == "jie":
            if regs[r]%2==0:
                pc+=int(offset)-1
        elif ins == "jio":
            if regs[r]==1:
                pc+=int(offset)-1
    return regs["b"]

print(run(0,0))
print(run(1,0))
