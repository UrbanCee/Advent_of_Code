
from functools import reduce
import operator
with open("inputs/day06.txt") as fp:
    lines = [line[:-1] for line in fp.readlines()]
    
task1Ops = list(map(list, zip(*[line.strip().split() for line in lines if len(line)>2]))) 
print("Task 1:",sum(reduce(operator.mul,map(int,op[:-1]),1) if op[-1]=="*" else sum(map(int,op[:-1])) for op in task1Ops))

task2Ops=[]
tempOp=[]
for i in range(len(lines[0])-1,-1,-1):
    numstring = "".join(lines[j][i] for j in range(len(lines)-1))
    if (numstring.count(" ")==len(numstring)):
        continue
    tempOp.append(numstring)
    if lines[-1][i] in {"+","*"}:
        tempOp.append(lines[-1][i])
        task2Ops.append(tempOp)
        tempOp=[]
print("Task 2:",sum(reduce(operator.mul,map(int,op[:-1]),1) if op[-1]=="*" else sum(map(int,op[:-1])) for op in task2Ops))
        
