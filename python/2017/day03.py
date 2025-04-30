import math
from size import *
input = 368078

def pos2coord(pos):
    inner=int(math.sqrt(pos-1)) if int(math.sqrt(pos-1))%2==1 else int(math.sqrt(pos-1))-1
    quadrant=(pos-inner*inner-1)//(inner+1)
    posinQuadrant=(pos-inner*inner-1)%(inner+1)
    if quadrant==0:
        return (inner//2+1,-(inner//2)+posinQuadrant)
    elif quadrant==1:
        return (inner//2-posinQuadrant,inner//2+1)
    elif quadrant==2:
        return (-(inner//2)-1,inner//2-posinQuadrant)
    else:
        return (-(inner//2)+posinQuadrant,-(inner//2)-1)

coord=pos2coord(input)
print("Task1: ",abs(coord[0])+abs(coord[1]))

values={(0,0):1,(1,0):1}
pos=2
while(values[pos2coord(pos)]<input):
    pos+=1
    values[pos2coord(pos)]=sum( [values.get(vAdd(pos2coord(pos),dir),0) for dir in dirs8] )

print("Task2: ",values[pos2coord(pos)])

