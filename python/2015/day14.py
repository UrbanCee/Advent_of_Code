import re
import numpy as np

rex = "([A-Za-z]+) can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds."

reindeers = {}
points = {}

with open("inputs/day14.txt") as fp:
    for line in fp.readlines():
        for name,speed,time,rest in re.findall(rex,line):
            reindeers[name]=(int(speed),int(time),int(rest)+int(time))

def calcDist(reindeer, time):
    speed,runtime,cycletime=reindeer
    return time//cycletime*speed*runtime + min(time%cycletime,runtime)*speed

print("Task1:",np.max([calcDist(deer,2503) for deer in reindeers.values()]))

for name in reindeers.keys():
    points[name]=0

for sec in range(1,2503):
    maxdist=np.max([calcDist(deer,sec) for deer in reindeers.values()])
    for name,deer in reindeers.items():
        if calcDist(deer,sec)==maxdist:
            points[name]+=1

print("Task2:",np.max([p for p in points.values()]))

