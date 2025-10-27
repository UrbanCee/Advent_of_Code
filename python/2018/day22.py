from queue import PriorityQueue as pq
from size import *
depth, target= 11109, (9,731)
#depth, target= 510, (10,10)
erosionLevels = dict()

def calcErosionLevel(coord):
    global erosionLevels
    if coord not in erosionLevels:
        erosionLevels[coord]=(geoIndex(coord)+depth)%20183
    return erosionLevels[coord]

def geoIndex(coord):
    if coord==target:
        return 0
    if coord[0]==0:
        return coord[1]*48271
    if coord[1]==0:
        return coord[0]*16807
    return calcErosionLevel((coord[0]-1,coord[1]))*calcErosionLevel((coord[0],coord[1]-1))
    
print("Task 1:",sum([calcErosionLevel((x,y))%3 for y in range(0,target[1]+1) for x in range(0,target[0]+1)]))
# rocky,neither = 0, wet,torch = 1, narrow,gear = 2 
nextPos,queuedPositions=pq(),{((0,0),1):0}
nextPos.put((0,((0,0),1)))
timeToTarget=[]

while not nextPos.empty():
    time,(currentPos,currentItem)=nextPos.get()
    if (currentPos==target): 
        timeToTarget.append(time if currentItem==1 else time+7)
        if len(timeToTarget)==3: break
    for dir in dirs4:
        newPos=vAdd(currentPos,dir)
        if newPos[0]<0 or newPos[1]<0: continue
        for item in range(3):
            nextTime=time+1+(0 if item == currentItem else 7)
            if (newPos,item) in queuedPositions:
                if queuedPositions[(newPos,item)]<=nextTime: continue
            if item == calcErosionLevel(newPos)%3: continue
            queuedPositions[(newPos,item)]=nextTime
            nextPos.put((nextTime,(newPos,item)))

print("Task 2:",min(timeToTarget))

