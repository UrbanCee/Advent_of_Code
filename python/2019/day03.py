import re
from size import *

dirmap = {"R":(1,0),"L":(-1,0),"U":(0,1),"D":(0,-1)}

def convert(str):
    for dirstr,dist in re.findall(r'([UDLR])(\d+)',str):
        return (dirmap[dirstr],int(dist))

with open("inputs/day03.txt") as fp:
    wirestrings = [[convert(str) for str in a.strip().split(",")] for a in fp.readlines()]

wire1 = {}
step=0
pos=(0,0)

for dir,length in wirestrings[0]:
   for i in range(length):
    step+=1
    pos = vAdd(pos,dir)
    if pos not in wire1:
        wire1[pos]=step

bestDist=0
pos=(0,0)
for dir,length in wirestrings[1]:
   for i in range(length):
    pos = vAdd(pos,dir)
    if pos in wire1 and pos != (0,0):
        if bestDist==0:
            bestDist=manDist(pos)
        elif manDist(pos)<bestDist:
            bestDist=manDist(pos)

print("Task1: ",bestDist)
          
