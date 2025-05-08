from itertools import combinations
import math

with open("inputs/day24.txt") as fp:
    weights = sorted([int(line) for line in fp.readlines() if len(line)>0],reverse=True)

def calc(numberOfGroups,groupSize=1):
    while len([x for x in combinations(weights,groupSize) if sum(x)==sum(weights)//numberOfGroups])==0: groupSize+=1
    return min([math.prod(fstGroupWeights) for fstGroupWeights in [x for x in combinations(weights,groupSize) if sum(x)==sum(weights)//numberOfGroups]])

print("Task 1:",calc(3))
print("Task 2:",calc(4))