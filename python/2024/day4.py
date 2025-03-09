from size import *

f1="inputs/day4_training.txt"
f2="inputs/day4.txt"

with open(f2,"rt") as fp:
    lines = fp.readlines()

xmasfield = "".join(map(str.strip,lines))
s = mySize(len(lines[0].strip()),len(lines))

dirs = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
xmas = "XMAS"

count1 = 0
for i in range(s.w*s.h):
    pos = s.toVec(i)
    if (xmasfield[i]==xmas[0]):
        for dir in dirs:
            if not s.outOfBoundsv(vAdd(pos,vMul(dir,3))):
                for j in range(1,len(xmas)):
                    if xmas[int(j)]!=xmasfield[int(s.toIndv(vAdd(pos,vMul(dir,j))))]:
                        break
                    if j==(len(xmas)-1):
                        count1=count1+1

def checkdia(pos,dia):
    return ((xmasfield[s.toIndv(vAdd(pos,dia[0]))]=="S" and xmasfield[s.toIndv(vAdd(pos,dia[1]))]=="M") or 
            (xmasfield[s.toIndv(vAdd(pos,dia[1]))]=="S" and xmasfield[s.toIndv(vAdd(pos,dia[0]))]=="M"))

((-1,-1),(1,1))
((-1,1),(1,-1))
count2 = 0
for cy in range(1,s.h-1):
    for cx in range(1,s.w-1):
        if (xmasfield[s.toInd(cx,cy)]=="A"):
            if (checkdia((cx,cy),((-1,-1),(1,1))) and checkdia((cx,cy),((-1,1),(1,-1)))):
                count2=count2+1
                


print("task1:",count1)
print("task1:",count2)
    


