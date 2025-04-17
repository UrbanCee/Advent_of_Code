import json as js

def traverse(d,ignoreRed):
    value = 0
    if isinstance(d,int):
        return d
    elif isinstance(d,list):
        for ld in d:
            value += traverse(ld,ignoreRed)
    elif isinstance(d,dict):
        for k,v in d.items():
            if ignoreRed and isinstance(v,str) and v=="red":
                return 0
            value += traverse(v,ignoreRed)
    return value

with open("inputs/day12.txt") as fp:
    data = js.loads(fp.read())

print("Task1: ",traverse(data,False))
print("Task2: ",traverse(data,True))
