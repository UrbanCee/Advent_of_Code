import re

rectEx = "(rect|rotate row|rotate column)[ xy=]*(\\d+)[x by]*(\\d+)*"
width, height = 50,6
playfield = [[False for i in range(width)] for j in range(height)]

with open("inputs/day08.txt") as fp:
    cmds = [(cmd,int(x),int(y)) for line in fp.readlines() for cmd,x,y in re.findall(rectEx,line)]

def rect(pf,x,y):
    for j in range(y):
        for i in range(x):
            pf[j][i]=True

def rotateColumn(pf,col,offset):
    columnData=[pf[j][col] for j in range(height)]
    for j in range(height):
        pf[j][col]=columnData[(j+(height-offset))%height]
    
def rotateRow(pf,row,offset):
    rowData=pf[row]
    pf[row]=[rowData[(i+(width-offset))%width] for i in range(width)]

for cmd,x,y in cmds:
    if cmd=="rect":
        rect(playfield,x,y)
    elif cmd=="rotate row":
        rotateRow(playfield,x,y)
    else:
        rotateColumn(playfield,x,y)

print("Task1: ",sum(led for row in playfield for led in row))
for line in ["".join(map(lambda x:'#' if x else ' ',row)) for row in playfield]: print(line)


