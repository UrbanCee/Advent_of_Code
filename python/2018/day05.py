import re
with open("inputs/day05.txt") as fp:
    polymer=fp.read().strip()

def reduceStep(poly):
    reducedPoly,currentPos=[],0
    while (currentPos<len(poly)):
        if currentPos==len(poly)-1 or abs(ord(poly[currentPos])-ord(poly[currentPos+1]))!=ord("a")-ord("A"):
            reducedPoly.append(poly[currentPos])
            currentPos+=1
        else: currentPos+=2
    return "".join(reducedPoly)

def reduce(poly):
    beforestep,afterstep=str(poly),reduceStep(poly)
    while afterstep!=beforestep:
        newstring=reduceStep(afterstep)
        beforestep=afterstep
        afterstep=newstring
    return afterstep

print("Task1 :",len(reduce(polymer)))
polyGroups=[f"[{chr(x)}{chr(x+ord("a")-ord("A"))}]" for x in range(ord("A"),ord("Z")+1)]
print("Task2 :",min([len(reduce(re.sub(group,"",polymer))) for group in polyGroups]))

