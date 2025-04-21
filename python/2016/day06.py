
charInvs =[{},{},{},{},{},{},{},{}]

with open("inputs/day06.txt") as fp:
    for line in list(map(str.strip,fp.readlines())):
        for i in range(len(line)):
            currDict=charInvs[i]
            if line[i] not in currDict.keys():
                currDict[line[i]]=1
            else:
                currDict[line[i]]=currDict[line[i]]+1
            charInvs[i]=currDict


print("Task1: ","".join([sorted([(ch,num) for ch,num in charInv.items()],key=lambda x: x[1],reverse=True)[0][0] for charInv in charInvs]))
print("Task2: ","".join([sorted([(ch,num) for ch,num in charInv.items()],key=lambda x: x[1])[0][0] for charInv in charInvs]))