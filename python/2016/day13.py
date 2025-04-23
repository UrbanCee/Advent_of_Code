from size import *
from collections import deque as dq

input=1362

def isWall(v):
    x,y=v[0],v[1]
    value=x*x+3*x+2*x*y+y+y*y+input
    return sum([(value & divisor)>0 for divisor in [1<<power for power in range(64)]])%2==1

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
dists = {(1,1):0}
locations = set((1,1))

pos=(1,1)
nextPos=dq()
while pos!=(31,39):
    for dir in dirs:
        newPos=vAdd(pos,dir)
        if newPos[0]>=0 and newPos[1]>=0 and newPos not in dists.keys() and not isWall(newPos):
            nextPos.append((newPos,dists[pos]+1))
    pos,dist=nextPos.popleft()
    if dist<=50:
        locations.add(pos)
    dists[pos]=dist

print("Task1: ",dists[(31,39)])
print("Task2: ",len(locations))
    



