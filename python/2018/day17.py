import re
from collections import deque
with open("inputs/day17.txt") as fp:
    claycoords = {(int(c1),c) if xy=='x' else (c,int(c1)) for xy,c1,cs,ce in re.findall(r'([xy])=(\d+), [xy]=(\d+)\.\.(\d+)',fp.read().strip()) for c in range(int(cs),int(ce)+1)}
    rect=((min([x for x,_ in claycoords]),min([y for _,y in claycoords])),(max([x for x,_ in claycoords]),max([y for _,y in claycoords])))
def printVessels(water):
    for y in range(rect[0][1],rect[1][1]+1):
        print("".join(["#" if (x,y) in claycoords else "~" if (x,y) in water else "." for x in range(rect[0][0]-1,rect[1][0]+2)]))


def startFill(source,water):
    for y in range(source[1],rect[1][1]+1):
        if rect[0][1]<=y<=rect[1][1]:
            water.add((source[0],y))
        if (source[0],y+1) in claycoords:
            return (source[0],y)
    return (source[0],-1)
def checkOverflow(source,water,sources):
    for dir in [1,-1]:
        for x in [source[0]+offset*dir for offset in range(rect[1][0]-rect[0][0]+2)]:
            if (x,source[1]) in claycoords:
                break
            water.add((x,source[1]))
            if (x,source[1]+1) not in claycoords and (x,source[1]+1) not in water:
                sources.append((x,source[1]))
                break

water={(500,0)}
sources=deque()
sources.append((500,0))



print("Task 1:",len(water))