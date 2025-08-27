from size import *
import re

with open("inputs/day10.txt") as fp:
    satellites = [((int(x),int(y)),(int(vx),int(vy))) for line in fp.readlines() for x,y,vx,vy in re.compile(r'position=<\s*(\-*\d+),\s*(\-*\d+)> velocity=<\s*(\-*\d+),\s*(\-*\d+)>').findall(line)]

def bounding_box(satellites):
    return ((min(satellites,key=lambda k: k[0][0])[0][0],min(satellites,key=lambda k: k[0][1])[0][1]),(max(satellites,key=lambda k: k[0][0])[0][0],max(satellites,key=lambda k: k[0][1])[0][1]))
def spread(bounding_box):
    return (bounding_box[1][0]-bounding_box[0][0],bounding_box[1][1]-bounding_box[0][1])
def move(satellites):
    for i in range(0,len(satellites)):
        satellites[i]=(vAdd(satellites[i][0],satellites[i][1]),satellites[i][1])
def plot(satellites):
    box = bounding_box(satellites)
    print(box)
    for y in range(box[0][1],box[1][1]+1):
        print("".join(['#' if (x,y) in [(x,y) for ((x,y),(vx,vy)) in satellites] else '.' for x in range(box[0][0],box[1][0]+1)]))

minspread=spread(bounding_box(satellites))
minconst = satellites
mintime = 0

for i in range(1,11000):
    move(satellites)
    newSpread = spread(bounding_box(satellites))
    if newSpread[1]<minspread[1]:
        minspread=newSpread
        minconst=satellites.copy()
        mintime=i
        

plot(minconst)
print("Task 2:",mintime)

