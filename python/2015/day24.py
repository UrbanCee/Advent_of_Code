from itertools import combinations

with open("inputs/day24.txt") as fp:
    weights = sorted([int(line) for line in fp.readlines() if len(line)>0],reverse=True)

def mul(weights):
    result=1
    for el in weights:
        result*=el
    return result

def calc(numberOfGroups):
    groupWeight=sum(weights)//numberOfGroups
    for groupSize in range(len(weights)):
        possibleLists=[x for x in combinations(weights,groupSize) if sum(x)==groupWeight]
        if len(possibleLists)>0:
            break
    print("Task: ",min([mul(weights) for weights in possibleLists]))

calc(3)
calc(4)