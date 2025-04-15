from size import *

with open("inputs/day03.txt") as fp:
    line=fp.read()

delta = {"<":(-1,0),">":(1,0),"^":(0,1),"v":(0,-1)}
def moveAndVisit(curr,ch,vis):
    curr=vAdd(curr,delta[ch])
    vis.add(curr)
    return curr
    
visited={(0,0)}
currPos=(0,0)
for ch in line:
    currPos=moveAndVisit(currPos,ch,visited)
print("year1: visited houses:",len(visited))

currPositions=[(0,0),(0,0)]
visited.clear()
for pair in [line[i:i+2] for i in range(0,len(line),2)]:
    for j in range(2):
        currPositions[j]=moveAndVisit(currPositions[j],pair[j],visited)
print("year2: visited houses:",len(visited))
