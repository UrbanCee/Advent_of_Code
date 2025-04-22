with open("inputs/day17.txt") as fp:
    containers = [int(line) for line in fp.readlines()]

def fillEggNogg(index,amnt,numCont):
    cont = []
    for i in range(index,len(containers)):
        newAmnt=amnt+containers[i]
        if (newAmnt==150):
            cont.append(numCont+1)
        elif newAmnt<150:
            cont.extend(fillEggNogg(i+1,newAmnt,numCont+1))
    return cont

possible = fillEggNogg(0,0,0)
print("Task1 :",len(possible))
print("Task2 :",sum(map(lambda x:x==min(possible),possible)))
