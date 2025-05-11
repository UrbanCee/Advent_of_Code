from size import *
import hashlib
from queue import PriorityQueue

input="dmypynyp"

dirs={"U":(0,-1), "D":(0,1), "L":(-1,0), "R":(1,0)}
dir2Pos={"U":0, "D":1, "L":2, "R":3}

def possibleDirs(currPos,size,possDirs=""):
    for k,v in dirs.items():
        newPos=vAdd(currPos,v)
        if newPos[0]>=0 and newPos[0]<size and newPos[1]>=0 and newPos[1]<size:
            possDirs+=k
    return possDirs

def doorOpen(dir,travDirs):
    return ord(hashlib.md5(bytes(input+travDirs,"utf-8")).hexdigest()[dir2Pos[dir]])>=ord("b")

nextMove=PriorityQueue()
nextMove.put((0,((0,0),"")))
foundPaths = []

while not nextMove.empty():
    movedSteps,(pos,hist)=nextMove.get()
    if pos==(3,3):
        foundPaths.append(hist)
    else:
        for dir in possibleDirs(pos,4):
            if doorOpen(dir,hist):
                nextMove.put((len(hist),(vAdd(pos,dirs[dir]),hist+dir)))

possibleWays=sorted(foundPaths,key=len)
print("Task1: ",possibleWays[0])
print("Task2: ",len(possibleWays[-1]))
