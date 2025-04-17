from size import *
import numpy as np

input = ""
width=0
height=0

with open("inputs/day18.txt") as fp:
    for line in fp.readlines():
        height+=1
        width=len(line)
        input+=line.strip()

sz = mySize(width,height)

neighbors=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

def isOn(field,v):
    if sz.outOfBoundsv(v):
        return 0
    return field[sz.toIndv(v)]=="#"

def neighborCount(field,index):
    return np.sum([isOn(field,vAdd(sz.toVec(index),v)) for v in neighbors])

def turnOnCorners(field):
    for ind in [sz.toInd(0,0),sz.toInd(0,sz.h-1),sz.toInd(sz.w-1,0),sz.toInd(sz.w-1,sz.h-1)]:
        field=field[:ind] + "#" + field[ind + 1:]
    return field


def run(lightfield,steps,cornerson=False):
    if cornerson:
        lightfield=turnOnCorners(lightfield)
    for step in range(steps):
        newLightField = ""
        for i in range(len(lightfield)):
            nc = neighborCount(lightfield,i)
            if nc == 3 or (nc==2 and isOn(lightfield,sz.toVec(i))):
                newLightField+="#"
            else:
                newLightField+="."
        lightfield=newLightField
        if cornerson:
            lightfield=turnOnCorners(lightfield)
    return lightfield


print("Task1: ",run(str(input),100).count("#"))
print("Task1: ",run(str(input),100,True).count("#"))
