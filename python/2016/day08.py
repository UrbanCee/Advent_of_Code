import re

rectEx = "(rect|rotate row|rotate column)[ xy=]*(\\d+)[x by]*(\\d+)*"

cmds = []

with open("inputs/day08.txt") as fp:
    cmds = [(cmd,x,y) for line in fp.readlines() for cmd,x,y in re.findall(rectEx,line)]
    print(cmds)
    
