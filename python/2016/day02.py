from size import *

with open("inputs/day02.txt") as fp:
    lines=list(map(str.strip, fp.readlines()))

dirs = {"U":(0,-1),"R":(1,0),"D":(0,1),"L":(-1,0)}
buttons= [{(0,0):"1",(1,0):"2",(2,0):"3",(0,1):"4",(1,1):"5",(2,1):"6",(0,2):"7",(1,2):"8",(2,2):"9"},
        {(0,-2):"1",(-1,-1):"2",(0,-1):"3",(1,-1):"4",(-2,0):"5",(-1,0):"6",(0,0):"7",(1,0):"8",(2,0):"9",(-1,1):"A",(0,1):"B",(1,1):"C",(0,2):"D"}]
pos=[(1,1),(-2,0)]
code=["",""]

def addAndCheck(pos,dir,list):
    if vAdd(pos,dir) in list: return vAdd(pos,dir)
    else: return pos

for line in lines:
    for dir in [dirs[ch] for ch in line]: 
        for i in range(2):
            pos[i]=addAndCheck(pos[i],dir,buttons[i])
    code=[code[0]+buttons[0][pos[0]],code[1]+buttons[1][pos[1]]]

print("Task1: ",code[0])
print("Task2: ",code[1])
