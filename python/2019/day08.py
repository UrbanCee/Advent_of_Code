from size import *
from functools import reduce
s = mySize(25,6)
with open("inputs/day08.txt") as fp:
    imageRaw = fp.read().strip()
    layers = [imageRaw[i:i+s.w*s.h] for i in range(0,len(imageRaw),s.w*s.h)]

min0Layer=min(layers,key= lambda x: x.count("0"))
print("Task 1:",min0Layer.count("1")*min0Layer.count("2"))
s.print(reduce(lambda t,b: "".join([bi if t[i]=="2" else t[i] for i,bi in enumerate(b)]) ,layers).replace("0"," ").replace("1","X"))
