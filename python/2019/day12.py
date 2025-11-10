import re
import math
from size import *
with open("inputs/day12.txt") as fp:
    startpos=[(int(x),int(y),int(z))for x,y,z in re.findall(r'x=(\-?\d+), y=(\-?\d+), z=(\-?\d+)',fp.read())]

def calcVelChange(pos1:tuple[int,int,int],pos2:tuple[int,int,int],c:int):
    if pos1[c]==pos2[c]:return 0
    return math.copysign(1,(pos2[c]-pos1[c]))

def move(pos,vel):
    for pair in [(i,j) for i in range(len(pos)) for j in range(len(pos)) if i!=j]:
        vel[pair[0]]=tuple([vel[pair[0]][c]+calcVelChange(pos[pair[0]],pos[pair[1]],c) for c in range(3)]) 
    return [v3Add(pos[i],vel[i]) for i in range(len(pos))]  
def nrg(t): return sum(int(abs(t[i])) for i in range(len(t)))

pos, cyclic, steps =list(startpos),[0,0,0],0
vel=[(0,0,0) for _ in range(len(pos))]
while(cyclic[0]*cyclic[1]*cyclic[2]==0):
    pos=move(pos,vel)
    steps+=1
    if steps==1000: print("Task 1:",sum(nrg(pos[i])*nrg(vel[i]) for i in range(len(pos))))
    for c in [i for i in range(3) if cyclic[i]==0]:
        if sum(pos[i][c]==startpos[i][c] for i in range(len(pos)))==4:
            cyclic[c]=steps+1
print("Task 2:",math.lcm(*cyclic))


