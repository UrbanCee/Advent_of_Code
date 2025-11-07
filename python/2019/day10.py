from size import *

with open("inputs/day10.txt") as fp:
    array = [line.strip() for line in fp.readlines()]
    s = mySize(len(array[0]),len(array))
    field="".join(array)

def closestInDir(field,a,dir):
    while not s.outOfBoundsv(vAdd(a,dir)):
        a=vAdd(a,dir)
        if field[s.toIndv(a)]=="#":return a
    return None
def visibleAsteroids(field,a):
    return [closestInDir(field,s.toVec(a),findBase(vSub(s.toVec(p),s.toVec(a))))==s.toVec(p) for p in range(len(field)) if a!=p and field[p]!="."]

print("Task 1:",max( [sum(visibleAsteroids(field,a)) for a in range(len(field)) if field[a]!="."]))

        

