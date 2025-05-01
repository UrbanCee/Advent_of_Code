from size import *

with open("inputs/day11.txt") as fp:
    path = fp.read().strip().split(",")

dirs={"ne":(1,1),"n":(0,2),"nw":(-1,1),"se":(1,-1),"s":(0,-2),"sw":(-1,-1)}
maxdist=0
pos=(0,0)
for dir in path:
    pos=vAdd(pos,dirs[dir])
    maxdist=max(maxdist,abs(pos[0])+max(0,(abs(pos[1])-abs(pos[0]))//2))

print("Task1: ",abs(pos[0])+max(0,(abs(pos[1])-abs(pos[0]))//2))
print("Task2: ",maxdist)