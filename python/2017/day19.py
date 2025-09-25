from size import *

with open("inputs/day19.txt") as fp:
    input = [line.strip("\n") for line in fp.readlines() if len(line)>1]
    s = mySize(len(input[0]),len(input))
    input = "".join(input)

pos,dir,pipestring,steps=(input.index("|"),0),(0,1),"",0

while not s.outOfBoundsv(pos) and input[s.toIndv(pos)]!=" ":
    currChar=input[s.toIndv(pos)]
    if currChar not in {"-","|","+"}:
        pipestring+=currChar
    if currChar == "+":
        for dirIndex,newDirs,nextChar in [(0,{(-1,0),(1,0)},"-"),(1,{(0,1),(0,-1)},"|")]:
            if dir[dirIndex]==0:
                for newDir in newDirs:
                    newPos = vAdd(pos,newDir)
                    if not s.outOfBoundsv(newPos) and input[s.toIndv(newPos)]==nextChar:
                        dir=newDir
                break
    pos,steps=vAdd(pos,dir),steps+1

print("Task 1:",pipestring)
print("Task 2:",steps)


