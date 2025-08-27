import re

with open("inputs/day10_train.txt") as fp:
    satellites = [((int(x),int(y)),(int(vx),int(vy))) for line in fp.readlines() for x,y,vx,vy in re.compile(r'position=<\s*(\-*\d+),\s*(\-*\d+)> velocity=<\s*(\-*\d+),\s*(\-*\d+)>').findall(line)]

def bounding_box(satellites):
    return ((min(satellites,key=lambda k: k[0][0])[0][0],min(satellites,key=lambda k: k[0][1])[0][1]),(max(satellites,key=lambda k: k[0][0])[0][0],max(satellites,key=lambda k: k[0][1])[0][1]))

def move(satellites):
    for i in range(0,len(satellites)):
        ((x,y),(vx,vy))=satellites[i]
        satellites[i]=((x+vx,y+vy),(vx,vy))

move(satellites)
print(bounding_box(satellites))
