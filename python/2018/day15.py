from size import *
from queue import PriorityQueue as pq
with open("inputs/day15_train1.txt") as fp:
    input = [line.strip() for line in fp.readlines() if len(line.strip())>1]
    s = mySize(len(input[0]),len(input))
    room = [ c for line in input for c in line]
opp = {'G':'E','E':'G'}
hp = {i:200 for i,r in enumerate(room) if r in {'G','E'}}
initiativeOrder = [(r,i) for i,r in enumerate(room) if r in {'G','E'}]

s.print(room)
for eg,pos in initiativeOrder:
    if sum(room[s.addVecToInd(pos,dir)]==opp[eg] for dir in dirs4)==0: #no neighbor -> move
        print(eg,s.toVec(pos))
    