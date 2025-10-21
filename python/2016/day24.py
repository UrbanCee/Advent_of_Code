from size import *
from queue import PriorityQueue
import itertools as it

with open("inputs/day24.txt") as fp:
    lines = [line.strip() for line in fp.readlines()]
    s = mySize(len(lines[0]),len(lines))
    playfield="".join(lines)
    currpos=playfield.index("0")
    places = [str(i) for i in range(10) if str(i) in playfield]

def shortestPath(start,end):
    q = PriorityQueue()
    q.put((0,playfield.index(start)))
    queued={playfield.index(start)}
    while not q.empty():
        steps,curr=q.get()
        for dir in dirs4:
            newpos=s.addVecToInd(curr,dir)
            if newpos in queued:
                continue
            if playfield[newpos]==end:
                return steps+1
            if playfield[newpos]!="#":
                queued.add(newpos)
                q.put((steps+1,newpos))

pathLists = {places[i]+places[j]:shortestPath(places[i],places[j]) for i in range(len(places)) for j in range(i+1,len(places)) }

def calcMinS(endAt0):
    return min( [
        sum( [ pathLists["".join(sorted([(("0",*way,"0") if endAt0 else ("0",*way))[i],(("0",*way,"0") if endAt0 else ("0",*way))[i+1]]))] 
              for  i in range(len(way)+1 if endAt0 else len(way)) ] )
        for way in list(it.permutations([p for p in places if p!="0"]))    
    ])

print("Task 1:",calcMinS(False))
print("Task 2:",calcMinS(True))
