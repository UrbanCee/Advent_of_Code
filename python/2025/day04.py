from size import *
with open("inputs/day04.txt") as fp:
    lines = [line.strip() for line in fp.readlines() if len(line)>1]
    s,room,removed=mySize(len(lines[0]),len(lines)),[c for line in lines for c in line],set()

def canBeRemoved(idx):
    return idx not in removed and room[idx]=="@" and sum(s.outOfBoundsPlusOffset(idx,dir) or s.addVecToInd(idx,dir) in removed or room[s.addVecToInd(idx,dir)]=="." for dir in dirs8)>4

print("Task 1:",sum(canBeRemoved(i) for i in range(len(room))))
while(sum(canBeRemoved(i) for i in range(len(room)))>0):
    removed = removed.union({i for i in range(len(room)) if room[i]=="@" and canBeRemoved(i)})
print("Task 2:",len(removed))
    
