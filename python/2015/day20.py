import math

def divisors(house):
    lowElves = [i for i in range(1,int(math.sqrt(house))+1) if house%i==0]
    return lowElves+[house//i for i in lowElves if i*i!=house]

houses,targetPresents = 1,34000000

while(10*sum([x for x in divisors(houses)])<targetPresents):houses+=1
print("Task1: ",houses)
houses=1
while(11*sum([x for x in divisors(houses) if x*50>=houses])<targetPresents):houses+=1
print("Task2: ",houses)

