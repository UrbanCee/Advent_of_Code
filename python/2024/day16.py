from size import *

f1="inputs/day16_training_1.txt"
f2="inputs/day16_training_2.txt"
f3="inputs/day16.txt"

with open(f1,"rt") as fp:
    lines = fp.readlines()

playfield = "".join(map(str.strip,lines))
s = mySize(len(lines[0].strip()),len(lines))

def outputPlayfield():
    for y in range(s.w):
        print(playfield[y*s.w:(y+1)*s.w])
    
outputPlayfield()

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
start = (1,s.w-2)
curDir = 0
scorefield = {s.toIndv(start):[(0,0)]}

