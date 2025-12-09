import re
from itertools import combinations as co
with open("inputs/day09_train.txt") as fp:
    points = [(int(x),int(y)) for x,y in re.findall(r'(\d+),(\d+)',fp.read())]
rects = [((abs(p[0][0]-p[1][0])+1)*(abs(p[0][1]-p[1][1])+1),p) for p in co(points,2)]
horLines = [(pp[1],(min(pp[0],points[i+1][0]),max(pp[0],points[i+1][0]))) for i,pp in enumerate(points) if i <len(points)-1 and pp[1]==points[i+1][1]]
verLines = [(pp[0],(min(pp[1],points[i+1][1]),max(pp[1],points[i+1][1]))) for i,pp in enumerate(points) if i <len(points)-1 and pp[0]==points[i+1][0]]
print(verLines)

def notCrossing(r:tuple[tuple[int,int],tuple[int,int]]):
    return sum()+sum() == 0
    

print("Task 1:",max(rects,key=lambda x:x[0])[0])
print("Task 2:",max([r[0] for r in rects if notCrossing(r[1])],key=lambda x:x[0]))