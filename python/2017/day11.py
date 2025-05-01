from size import *
import itertools as it
import functools as fc

with open("inputs/day11.txt") as fp:
    path = fp.read().strip().split(",")

dirs={"ne":(1,1),"n":(0,2),"nw":(-1,1),"se":(1,-1),"s":(0,-2),"sw":(-1,-1)}

def distToZero(pos):
    return abs(pos[0])+max(0,(abs(pos[1])-abs(pos[0]))//2)

print("Task1: ",distToZero(fc.reduce(vAdd,[dirs[x] for x in path])))
print("Task2: ",max([distToZero(pos) for pos in it.accumulate([dirs[x] for x in path],vAdd)]))