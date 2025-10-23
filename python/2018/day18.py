from size import *
from collections import Counter
with open("inputs/day18.txt") as fp:
    playfield = "".join(s.strip() for s in fp.readlines() if len(s)>0)
s,storedPlayfields = mySize(50,50),{playfield:0}
def neighbors(currentStep,index):
    return dict(Counter([currentStep[s.addVecToInd(index,dir)] for dir in dirs8 if not s.outOfBoundsPlusOffset(index, dir) ]    ))
def evolveCell(cell,neighbors):
    if cell==".": return "|" if neighbors.get("|",0)>=3 else "."
    if cell=="|": return "#" if neighbors.get("#",0)>=3 else "|"
    else: return "#" if neighbors.get('#',0)>=1 and neighbors.get("|",0)>=1 else "."
def timestep(currentStep):
    return "".join([evolveCell(currentStep[i],neighbors(currentStep,i)) for i in range(len(currentStep)) ])

for i in range(1,10000):
    playfield=timestep(playfield)
    if i==10: print("Task1:",playfield.count("|")*playfield.count("#"))
    if playfield in storedPlayfields:
        finalIndex=(1000000000-storedPlayfields[playfield])%(i-storedPlayfields[playfield])+storedPlayfields[playfield]
        finalPlayfield=[(field,i) for field,i in storedPlayfields.items() if i==finalIndex][0]
        print("Task2:",finalPlayfield[0].count("|")*finalPlayfield[0].count("#"))
        break
    storedPlayfields[playfield]=i
        
    
