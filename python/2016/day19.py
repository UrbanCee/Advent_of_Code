import math

input= 3004953

elves=[i for i in range(1,input+1)]
while len(elves)>1:
    newElves = [elves[i] for i in range(0,len(elves),2)]
    elves=newElves[1:] if len(elves)%2==1 else newElves
print("Task1: ",elves[0])
print("Task2: ",input - 3 ** int(math.log(input)/math.log(3)))




#input=5
#curr=0
#for i in range(3,1000):
#    elves=[i for i in range(1,i+1)]
#    while len(elves)>1:
#        popIndex=(curr+len(elves)//2)%len(elves)
#        elves.pop(popIndex)
#        if curr<popIndex:
#            curr+=1
#        if curr==len(elves):
#            curr=0
#    print(f"{i}: {elves}")

