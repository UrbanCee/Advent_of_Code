from size import *

with open("inputs/day22.txt") as fp:
    lines = [line.strip() for line in fp.readlines() if len(line)>10]
    #lines = ["..#","#..","..."]
    w,h=len(lines[0]),len(lines)
    s=mySize(101,101)
    topleft=(s.w//2-w//2,s.h//2-h//2)
    grid = ['.' for i in range(s.w*s.h)]
    for x in range(w):
        for y in range(h):
            grid[s.toIndv(vAdd(topleft,(x,y)))]=lines[y][x]

def printGrid():
    for row in range(s.h):
        print("".join(grid[s.w*row:s.w*(row+1)]))

dirsLangton = [(0,-1),(1,0),(0,1),(-1,0)]
pos,dir,count=(s.w//2,s.h//2),0,0



for i in range(10000):
    if (grid[s.toIndv(pos)]=='#'):
        grid[s.toIndv(pos)]='.'
        dir=(dir+1)%4
    else:
        grid[s.toIndv(pos)]='#'
        dir=(dir+3)%4
        count+=1
    pos=vAdd(pos,dirsLangton[dir])

print("Task1: ",count)