import re
expr = re.compile("(\\d+)x(\\d+)x(\\d+)")

with open("inputs/day02.txt") as fp:
    dimensions = [tuple(sorted([int(xs),int(ys),int(zs)])) for line in fp.readlines() for xs,ys,zs in expr.findall(line)]

print("total paper:",sum([2*x*y+2*y*z+2*x*z+min(x*y,min(x*z,y*z)) for x,y,z in dimensions]))
print("total ribbon:",sum([2*(x+y)+x*y*z for x,y,z in dimensions]))
        
