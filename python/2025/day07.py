from size import *

with open("inputs/day07_train.txt") as fp:
    input = [l.strip() for l in fp.readlines() if len(l)>2]
    s=mySize(len(input[0]),len(input))
    input = [i for l in input for i in l]

input[input.index("S")+s.w]="|"
for r in range(2,len(input)):
    for i,c in enumerate(input[r*s.w:(r+1)*s.w]):
        if (input[s.toInd(i,r-1)]=="|"):
            if c=="^":
                input[s.toInd(i-1,r)]="|"
                input[s.toInd(i+1,r)]="|"
            if c==".": input[s.toInd(i,r)]="|"

print("Task 1:",sum(input[i-s.w]=="|" for i,c in enumerate(input) if c=="^"))

knownpaths = dict()
def countPaths(pos):
    for i in range(pos//s.w,s.h):
        if input[pos+i*s.w]=="^":
            

startPos = input.index("S")+s.w

