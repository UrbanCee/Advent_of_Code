import re
import numpy as np

expr = "(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)"

lights = [[False for i in range(1000)] for j in range(1000)]
brightnesses = [[0 for i in range(1000)] for j in range(1000)]

with open("inputs/day06.txt") as fp:
    for line in fp.readlines():
        for cmd,x1,y1,x2,y2 in re.findall(expr,line):
            for x in range(int(x1),int(x2)+1):
                for y in range(int(y1),int(y2)+1):
                    if cmd=="turn on":
                        lights[x][y]=True
                        brightnesses[x][y]+=1
                    elif cmd=="turn off":
                        lights[x][y]=False
                        brightnesses[x][y]-=1
                        brightnesses[x][y]=max(brightnesses[x][y],0)
                    else:
                        lights[x][y]= not lights[x][y]
                        brightnesses[x][y]+=2

print("Task1: On:",np.sum(lights))
print("Task1: Brightness:",np.sum(brightnesses))