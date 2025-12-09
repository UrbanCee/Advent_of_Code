import re
from itertools import combinations as co
with open("inputs/day09.txt") as fp:
    points = [(int(x),int(y)) for x,y in re.findall(r'(\d+),(\d+)',fp.read())]

print("Task 1:",max((abs(p[0][0]-p[1][0])+1)*(abs(p[0][1]-p[1][1])+1) for p in co(points,2)))
