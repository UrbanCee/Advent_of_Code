import re
with open("inputs/day05.txt") as fp:
    polymer=fp.read().strip()

removeGroups=[a+b for x in range(ord("A"),ord("Z")+1) for a,b in [chr(x)+chr(x+ord("a")-ord("A")),chr(x+ord("a")-ord("A"))+chr(x)] ]
def reduceStep(poly:str):
    for group in removeGroups:
        poly=poly.replace(group,"")
    return poly

def reduce(poly):
    beforestep,afterstep=str(poly),reduceStep(poly)
    while afterstep!=beforestep:
        newstring=reduceStep(afterstep)
        beforestep=afterstep
        afterstep=newstring
    return afterstep

print("Task1 :",len(reduce(polymer)))
polyGroups=[re.compile(f"[{chr(x)}{chr(x+ord("a")-ord("A"))}]") for x in range(ord("A"),ord("Z")+1)]
print("Task2 :",min([len(reduce(group.sub("",polymer))) for group in polyGroups]))

