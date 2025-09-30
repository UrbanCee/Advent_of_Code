import re
from math import *

with open("inputs/day23.txt") as fp:
    program = [(cmd,a,b) for line in fp.readlines() for cmd,a,b in re.findall(r'(set|sub|mul|jnz) (-?[a-z0-9]*) ?(-?[a-z0-9]*)?',line)]

cmdMap = {"set":lambda x ,y: y, "sub": lambda x,y:x-y, "mul": lambda x,y:x*y}

def evalArg(arg:str,r:dict):
    return (int(arg) if arg.lstrip("-").isnumeric() else r.get(arg,0))

def run(pc,r:dict):
    countmul=0
    while 0<=pc<len(program):
        cmd,a,b = program[pc]
        if cmd in cmdMap:
            r[a]=cmdMap[cmd](evalArg(a,r),evalArg(b,r))
        if cmd=="mul":
            countmul+=1
        pc += evalArg(b,r) if cmd == "jnz" and evalArg(a,r)!=0 else 1
    return countmul

print("Task 1:",run(0,dict()))
def notPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return True
    return False
bvalue=int(program[0][2])*100+100000
print(bvalue)
print("Task 2:",sum([notPrime(i) for i in range(bvalue,bvalue+17017,17)]))
