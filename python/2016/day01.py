import re
from size import *

with open("inputs/day01.txt") as fp:
    input=fp.read()

expr = "([L|R])(\\d+)"
dirs,dir,visited,pos,firstDoublePos = [(0,1),(1,0),(0,-1),(-1,0)],0,{(0,0)},(0,0),(0,0)
dirOffset={"R":1,"L":3}

for lr,dist in re.findall(expr,input):
    dir = (dir + dirOffset[lr]) % 4
    for i in range(int(dist)):
        pos = vAdd(pos,dirs[dir])
        if firstDoublePos==(0,0) and pos in visited:
            firstDoublePos = pos
        visited.add(pos)

print("Task1: ",manDist(pos))
print("Task1: ",manDist(firstDoublePos))

