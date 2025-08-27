from size import *

serialNumber = 1723

def power(x,y):
    return ((((x+10)*y+serialNumber)*(x+10))%1000)//100-5

maxpos = (0,0,0)
max=0

for ra in range(150,151):
    for y in range(1,301-ra):
        for x in range(1,301-ra):
            powersum=0
            for cy in range(0,ra):
                for cx in range(0,ra):
                    powersum+=power(x+cx,y+cy)
            if powersum > max:
                max=powersum
                maxpos=(x,y,ra)


print("Task 1: ",maxpos)