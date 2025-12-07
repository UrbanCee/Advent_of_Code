
from functools import reduce
import operator
with open("inputs/day06_train.txt") as fp:
    input = [line.strip().split() for line in fp.readlines() if len(line)>2]
    ops = list(map(list, zip(*input)))
    

print("Task 1:",sum(reduce(operator.mul,map(int,op[:-1]),1) if op[-1]=="*" else sum(map(int,op[:-1])) for op in ops))

