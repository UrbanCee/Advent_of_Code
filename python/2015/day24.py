from itertools import combinations
import math

with open("inputs/day24.txt") as fp:
    weights = sorted([int(line) for line in fp.readlines() if len(line)>0],reverse=True)

def calc(numberOfGroups):
    possibleLists,groupSize=[],1
    while len(possibleLists)==0:
        possibleLists=[x for x in combinations(weights,groupSize) if sum(x)==sum(weights)//numberOfGroups]
        groupSize+=1
    return min([math.prod(fstGroupWeights) for fstGroupWeights in possibleLists])

print("Task 1:",calc(3))
print("Task 2:",calc(4))