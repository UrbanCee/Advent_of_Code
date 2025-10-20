import re
from size import *
with open("inputs/day23.txt") as fp:
    robots = [((int(x),int(y),int(z)),int(r)) for line in fp.readlines() for x,y,z,r in re.findall(r'pos=<(\-?\d+),(\-?\d+),(\-?\d+)>, r=(\d+)',line)]

def mandist(x,y): return abs(x[0]-y[0])+abs(x[1]-y[1])+abs(x[2]-y[2])
strongest = max(robots, key=lambda r: r[1])
print("Task 1: ",len([r for r in robots if mandist(r[0],strongest[0])<=strongest[1]]))
