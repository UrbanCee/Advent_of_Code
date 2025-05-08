charInvs =[{},{},{},{},{},{},{},{}]

with open("inputs/day06.txt") as fp:
    for line in list(map(str.strip,fp.readlines())):
        for i in range(len(line)):
            charInvs[i][line[i]]=charInvs[i].get(line[i],0)+1




print("Task1: ","".join([sorted([(ch,num) for ch,num in charInv.items()],key=lambda x: x[1],reverse=True)[0][0] for charInv in charInvs]))
print("Task2: ","".join([sorted([(ch,num) for ch,num in charInv.items()],key=lambda x: x[1])[0][0] for charInv in charInvs]))