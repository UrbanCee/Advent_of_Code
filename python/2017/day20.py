from size import *
from itertools import combinations as cb
from collections import defaultdict
import re
rex=re.compile(r'p=<(-?[0-9]*),(-?[0-9]*),(-?[0-9]*)>, v=<(-?[0-9]*),(-?[0-9]*),(-?[0-9]*)>, a=<(-?[0-9]*),(-?[0-9]*),(-?[0-9]*)>')
with open("inputs/day20.txt") as fp:
    buffer = [((int(px),int(py),int(pz)),(int(vx),int(vy),int(vz)),(int(ax),int(ay),int(az))) for px,py,pz,vx,vy,vz,ax,ay,az in rex.findall(fp.read())]

validParticles = {i for i in range(len(buffer))}

for ticks in range(5000):
    posDict = defaultdict(list)
    for i in range(len(buffer)):
        p,v,a = buffer[i]
        v=v3Add(v,a)
        p=v3Add(p,v)
        buffer[i]=(p,v,a)
        if i in validParticles:
            posDict[p].append(i)
    for idx in [idx for idxAtPos in posDict.values() for idx in idxAtPos if len(idxAtPos)>1]:
        validParticles.remove(idx)

print("Task 1: ",min([(i,man3Dist(buffer[i][0])) for i in range(len(buffer))],key=lambda x:x[1])[0])
print("Task 2: ",len(validParticles))