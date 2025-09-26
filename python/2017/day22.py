from size import *

with open("inputs/day22.txt") as fp:
    lines = [line.strip() for line in fp.readlines() if len(line)>10]
    #lines = ["..#","#..","..."]
    w,h=len(lines[0]),len(lines)
    s=mySize(501,501)
    topleft=(s.w//2-w//2,s.h//2-h//2)
    grid = ['.' for i in range(s.w*s.h)]
    for x in range(w):
        for y in range(h):
            grid[s.toIndv(vAdd(topleft,(x,y)))]=lines[y][x]

def printGrid():
    for row in range(s.h):
        print("".join(grid[s.w*row:s.w*(row+1)]))

dirsLangton = [(0,-1),(1,0),(0,1),(-1,0)]

def run(grid,steps,nextstate:dict,diroffset:dict):
    pos,dir,count=(s.w//2,s.h//2),0,0
    for i in range(steps):
        dir=(dir+diroffset[grid[s.toIndv(pos)]])%4
        grid[s.toIndv(pos)]=nextstate[grid[s.toIndv(pos)]]
        if (grid[s.toIndv(pos)]=='#'):
            count+=1
        pos=vAdd(pos,dirsLangton[dir])
    return count


print("Task1: ",run(grid.copy(),10000,{".":"#","#":"."},{".":3,"#":1}))
print("Task2: ",run(grid.copy(),10000000,{".":"W","W":"#","#":"F","F":"."},{".":3,"W":0,"#":1,"F":2}))