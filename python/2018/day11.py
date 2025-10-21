from size import *
serialNumber = 1723
def power(x,y):
    return ((((x+10)*y+serialNumber)*(x+10))%1000)//100-5
powersums = [power(x,y) for y in range(300) for x in range(300)]
def boundedValue(x,y):
    return 0 if y<0 or x<0 else powersums[y*300+x]
for y in range(300): 
    for x in range(300):
        powersums[y*300+x]=powersums[y*300+x]+boundedValue(x,y-1)+boundedValue(x-1,y)-boundedValue(x-1,y-1)
def findMaxiumSum(offset):
    return max([(x,y,boundedValue(x-1,y-1)+boundedValue(x+offset,y+offset)-boundedValue(x-1,y+offset)-boundedValue(x+offset,y-1))for y in range(300-offset)for x in range(300-offset)],key = lambda x:x[2])
print("Task 1: ",findMaxiumSum(2))
print("Task 2: ",max( [(findMaxiumSum(offset),offset+1) for offset in range(1,100)] , key = lambda x: x[0][2]))