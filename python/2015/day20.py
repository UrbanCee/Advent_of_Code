import math
import numpy as np

def divisors(house):
    lowElves = [i for i in range(1,int(math.sqrt(house))+1) if house%i==0]
    highElves = [house//i for i in lowElves if i*i!=house]
    return lowElves+highElves

task1, task2 = 0,0
houses=1
targetPresents=34000000

while task1==0 or task2==0:
    divs=divisors(houses)
    if task1==0:
        if 10*np.sum([x for x in divs])>=targetPresents:
            task1=houses
    if task2==0:
        if 11*np.sum([x for x in divs if x*50>=houses])>=targetPresents:
            task2=houses
    houses+=1
print("Task1: ",task1)
print("Task2: ",task2)
