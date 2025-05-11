import re

insRex = re.compile(r'(hlf|tpl|inc|jmp|jie|jio) (a|b)*[, ]*\+?([-]*\d+)*')
ops = {"hlf": lambda x:x//2, "tpl":lambda x:x*3, "inc":lambda x:x+1}

with open("inputs/day23.txt") as fp:
    program = [(ins,reg,offset) for line in fp.readlines() for ins,reg,offset in insRex.findall(line)]

def run(regs,pc=0):
    while(pc<len(program)):
        ins,r,offset = program[pc]
        if ins in ops.keys():
            regs[r]=ops[ins](regs[r])
        if ins == "jmp" or (ins == "jie" and regs[r]%2==0) or (ins == "jio" and regs[r]==1):
            pc+=int(offset)
        else: pc+=1
    return regs["b"]

print("Task1:",run({"a":0, "b":0}))
print("Task2:",run({"a":1, "b":0}))