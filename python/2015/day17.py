import numpy as np

containers = []

with open("inputs/day17.txt") as fp:
    for line in fp.readlines():
        containers.append(int(line))

def fillEggNogg(index,amnt,numCont):
    cont = []
    for i in range(index,len(containers)):
        newAmnt=amnt+containers[i]
        if (newAmnt>=150):
            if (newAmnt==150):
                cont.append(numCont+1)
            continue
        else:
            cont.extend(fillEggNogg(i+1,newAmnt,numCont+1))
    return cont

possible = fillEggNogg(0,0,0)
minCont = np.min(possible)
print("Task1 :",len(possible))
print("Task2 :",len([n for n in possible if n==minCont]))