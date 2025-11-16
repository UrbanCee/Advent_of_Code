import re
from size import *
from collections import Counter
with open("inputs/day06.txt") as fp:
    coords = [(int(x),int(y)) for line in fp.readlines() for x,y in re.compile(r'(\d+), (\d+)').findall(line)]
def minindex(pos):
    distInd=[(manDist(vSub(pos,ci)),i) for i,ci in enumerate(coords)]
    mindist = min(distInd,key=lambda d:d[0])
    return mindist[1] if sum([dI[0]==mindist[0] for dI in distInd ])==1 else -1
s = mySize(max([x for x,_ in coords])+2,max([y for _,y in coords])+2)
voronoifield=[minindex((x,y)) for y in range(s.h) for x in range(s.w)]
infty = {voronoifield[s.toInd(x,0)] for x in range(s.w)}.union({voronoifield[s.toInd(x,s.h-1)] for x in range(s.w)}).union({voronoifield[s.toInd(0,y)] for y in range(s.h)}).union({voronoifield[s.toInd(s.w-1,y)] for y in range(s.h)})
sizes = {k:v for k,v in dict(Counter(voronoifield)).items() if k not in infty}
print("Task 1:",sizes[max(sizes,key=sizes.get)])
print("Task 2:",sum([sum([manDist(vSub(c,(x,y))) for c in coords])<10000 for y in range(s.h) for x in range(s.w)]))





