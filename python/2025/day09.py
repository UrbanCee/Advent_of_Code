import re
from itertools import combinations as co
with open("inputs/day09_train.txt") as fp:
    points = [(int(x),int(y)) for x,y in re.findall(r'(\d+),(\d+)',fp.read())]
def sortRect(r:tuple[tuple[int,int],tuple[int,int]]):return ((min(r[0][0],r[1][0]),min(r[0][1],r[1][1])),(max(r[0][0],r[1][0]),max(r[1][1],r[1][1])))
rects = [((abs(p[0][0]-p[1][0])+1)*(abs(p[0][1]-p[1][1])+1),sortRect(p)) for p in co(points,2)] # A,(p1,p2)
horLines = [(pp[1],(min(pp[0],points[i+1][0]),max(pp[0],points[i+1][0]))) for i,pp in enumerate(points) if i <len(points)-1 and pp[1]==points[i+1][1]]
verLines = [(pp[0],(min(pp[1],points[i+1][1]),max(pp[1],points[i+1][1]))) for i,pp in enumerate(points) if i <len(points)-1 and pp[0]==points[i+1][0]]
print(verLines)
print(horLines)

def notCrossing(r:tuple[tuple[int,int],tuple[int,int]]):
    crossings=sum(x>r[0][0] and x<r[1][0] and r[0][1]<yh and r[0][1]>yl for x,(yl,yh) in verLines)
    crossings+=sum(x>r[0][0] and x<r[1][0] and r[1][1]<yh and r[1][1]>yl for x,(yl,yh) in verLines)
    crossings+=sum(y>r[0][1] and y<r[1][1] and r[0][0]<xh and r[0][0]>xl for y,(xl,xh) in horLines)
    crossings+=sum(y>r[0][1] and y<r[1][1] and r[1][0]<xh and r[1][0]>xl for y,(xl,xh) in horLines)
    print(crossings,r)
    return crossings == 0
    

print("Task 1:",max(rects,key=lambda x:x[0])[0])
print("Task 2:",max([r for r in rects if notCrossing(r[1])],key=lambda x:x[0]))