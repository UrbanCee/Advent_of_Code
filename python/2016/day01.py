import re
from size import *

with open("inputs/day01.txt") as fp:
    input=fp.read()

expr = "([L|R])(\\d+)"

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
pos = (0,0)
dir = 0
visited = {(0,0)}
firstDoublePos = (0,0)

for lr,dist in re.findall(expr,input):
    if lr == "R": dir=(dir+1)%4
    else: dir = (dir+3)%4
    for i in range(int(dist)):
        pos = vAdd(pos,dirs[dir])
        if firstDoublePos==(0,0) and pos in visited:
            firstDoublePos = pos
        visited.add(pos)

print("Task1: ",manDist(pos))
print("Task1: ",manDist(firstDoublePos))