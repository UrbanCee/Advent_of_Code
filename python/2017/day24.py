import re

with open("inputs/day24.txt") as fp:
    elements = [(int(i),int(j)) for line in fp.readlines() for i,j in re.findall(r'(\d*)/(\d*)',line)]

bestStrength=0
bestLength=0
bestLongStrength=0

def findNext(found,nextcomponent,currentStrength):
    end=True
    global bestStrength,bestLength,bestLongStrength
    for elem in [e for e in elements if e not in found]:
        for compInd in range(2):
            if elem[compInd]==nextcomponent:
                findNext(found+[elem],elem[1-compInd],currentStrength+sum(elem))
                end=False
    if end:
        bestStrength=max(bestStrength,currentStrength)
        if len(found)>bestLength:
            bestLength=len(found)
            bestLongStrength=currentStrength
        elif len(found)==bestLength:
            bestLongStrength=max(bestLongStrength,currentStrength)

findNext([],0,0)
print("Task 1:",bestStrength)
print("Task 2:",bestLongStrength)

