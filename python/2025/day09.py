import re
from itertools import combinations as co
with open("inputs/day09.txt") as fp:
    points = [(int(x),int(y)) for x,y in re.findall(r'(\d+),(\d+)',fp.read())]
rects = [((abs(p[0][0]-p[1][0])+1)*(abs(p[0][1]-p[1][1])+1),p) for p in co(points,2)]

print("Task 1:",max(rects,key=lambda x:x[0])[0])
