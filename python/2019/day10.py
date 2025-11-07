from size import *
import math

with open("inputs/day10.txt") as fp:
    array = [line.strip() for line in fp.readlines()]
    s = mySize(len(array[0]),len(array))
    field="".join(array)

def closestInDir(field,a,dir,vaporized):
    while not s.outOfBoundsv(vAdd(a,dir)):
        a=vAdd(a,dir)
        if field[s.toIndv(a)]=="#" and a not in vaporized:return a
    return None
def visibleAsteroids(field,a,vaporized):
    return [p for p in range(len(field)) if a!=p and field[p]!="." and closestInDir(field,s.toVec(a),findBase(vSub(s.toVec(p),s.toVec(a))),vaporized)==s.toVec(p)]

vaporized=set()
bestStation=max( [(len(visibleAsteroids(field,a,set())),a) for a in range(len(field)) if field[a]!="."],key=lambda x:x[0])

print("Task 1: location",s.toVec(bestStation[1]),"sees other asteroids:",bestStation[0])
while len(vaporized)<200:
    for toVap in sorted(visibleAsteroids(field,bestStation[1],vaporized),key=lambda x: math.atan2(s.vecTo(bestStation[1],x)[0],-s.vecTo(bestStation[1],x)[1])% (2 * math.pi)):
        vaporized.add(toVap)
        if len(vaporized)==200:
            print("Task 2:",s.toVec(toVap),"  score:",s.toVec(toVap)[0]*100+s.toVec(toVap)[1])
        

