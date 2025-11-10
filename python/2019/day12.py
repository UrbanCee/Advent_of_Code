import re
import math
from size import *
with open("inputs/day12_train.txt") as fp:
    startpos=[(int(x),int(y),int(z))for x,y,z in re.findall(r'x=(\-?\d+), y=(\-?\d+), z=(\-?\d+)',fp.read())]
    pos=list(startpos)
    vel=[(0,0,0) for _ in range(len(pos))]

def calcVelChange(pos1:tuple[int,int,int],pos2:tuple[int,int,int],c:int):
    if pos1[c]==pos2[c]:return 0
    return math.copysign(1,(pos2[c]-pos1[c]))

def move(pos,vel):
    for pair in [(i,j) for i in range(len(pos)) for j in range(len(pos)) if i!=j]:
        vel[pair[0]]=tuple([vel[pair[0]][c]+calcVelChange(pos[pair[0]],pos[pair[1]],c) for c in range(3)]) 
    return [v3Add(pos[i],vel[i]) for i in range(len(pos))]  
def nrg(t): return sum(int(abs(t[i])) for i in range(len(t)))

for i in range(1000): pos = move(pos,vel)
print("Task 1:",sum(nrg(pos[i])*nrg(vel[i]) for i in range(len(pos))))

print(startpos)
vel=[(0,0,0) for _ in range(len(pos))]
pos=list(startpos)
cyclic=[0 for _ in range(len(pos))]
steps=0
while(cyclic[0]*cyclic[1]*cyclic[2]*cyclic[3]==0):
    pos=move(pos,vel)
    steps+=1
    for c in [i for i in range(len(pos)) if cyclic[i]==0]:
        if pos[c]==startpos[c]:
            cyclic[c]=steps+1
            print(cyclic)
            print(pos,startpos)
print(cyclic)
print(math.lcm(*cyclic))


