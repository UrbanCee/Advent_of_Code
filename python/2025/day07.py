from size import *

with open("inputs/day07.txt") as fp:
    input = [l.strip() for l in fp.readlines() if len(l)>2]
    s=mySize(len(input[0]),len(input))
    input = [i for l in input for i in l]

splits = 0
knownpaths = dict()
def countPaths(pos):
    global splits
    if s.toVec(pos)[1]==s.w-1:
        return 1
    if pos in knownpaths: return knownpaths[pos]
    if input[pos+s.w]=="^":
        paths=countPaths(pos+s.w+1)+countPaths(pos+s.w-1)
        splits+=1
    else:
        paths=countPaths(pos+s.w)
    knownpaths[pos]=paths
    return paths

print("Task 2:",countPaths(input.index("S")))
print("Task 1:",splits)
