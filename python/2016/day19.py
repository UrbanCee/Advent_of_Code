input= 3004953

elves=[i for i in range(1,input+1)]
while len(elves)>1:
    newElves = [elves[i] for i in range(0,len(elves),2)]
    elves=newElves[1:] if len(elves)%2==1 else newElves
print("Task1: ",elves[0])


