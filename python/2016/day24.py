from size import *
from queue import PriorityQueue

with open("inputs/day24_train.txt") as fp:
    lines = [line.strip() for line in fp.readlines()]
    s = mySize(len(lines[0]),len(lines))
    playfield="".join(lines)
    currpos=playfield.index("0")
    places = [str(i) for i in range(10) if str(i) in playfield]

def shortestPath(start,end):
    q = PriorityQueue()
    q.put((0,playfield.index(start)))
    visited=set()
    while not q.empty():
        steps,curr=q.get()
        visited.add(curr)
        for dir in dirs4:
            newpos=s.addVecToInd(curr,dir)
            if newpos in visited:
                continue
            if playfield[newpos]==end:
                return steps+1
            if playfield[newpos]!="#":
                q.put((steps+1,newpos))

pathLists = {places[i]+places[j]:shortestPath(places[i],places[j]) for i in range(len(places)) for j in range(i+1,len(places)) }

