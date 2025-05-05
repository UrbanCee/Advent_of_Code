import math

def divisors(house):
    lowElves = [i for i in range(1,int(math.sqrt(house))+1) if house%i==0]
    return lowElves+[house//i for i in lowElves if i*i!=house]

task,houses,targetPresents = [0,0],1,34000000

while task[0]*task[1]==0:
    divs=divisors(houses)
    if task[0]==0:
        if 10*sum([x for x in divs])>=targetPresents:
            task[0]=houses
    if task[1]==0:
        if 11*sum([x for x in divs if x*50>=houses])>=targetPresents:
            task[1]=houses
    houses+=1
print("Task1: ",task[0])
print("Task2: ",task[1])
