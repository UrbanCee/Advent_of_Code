import re

paper = 0
ribbon = 0
expr = "(\\d+)x(\\d+)x(\\d+)"

with open("inputs/day02.txt") as fp:
    for line in fp.readlines():
        match=re.search(expr,line)
        x,y,z=int(match[1]),int(match[2]),int(match[3])
        paper+=2*x*y+2*y*z+2*x*z+min(x*y,min(x*z,y*z))
        sortedDim=sorted([x,y,z])
        ribbon+=2*(sortedDim[0]+sortedDim[1])+x*y*z

print("total paper:",paper)
print("total ribbon:",ribbon)
        
