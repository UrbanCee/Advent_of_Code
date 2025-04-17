import re
import numpy as np

rex = "^Sue (\\d+): ([A-Za-z]+): (\\d+), ([A-Za-z]+): (\\d+), ([A-Za-z]+): (\\d+)$"

sues = {}
realSue = {"children": 3,"cats": 7,"samoyeds": 2,"pomeranians": 3,"akitas": 0,"vizslas": 0,"goldfish": 5,"trees": 3,"cars": 2,"perfumes": 1}

with open("inputs/day16.txt") as fp:
    for line in fp.readlines():
        for (sue,p1,v1,p2,v2,p3,v3) in re.findall(rex,line):
            sues[sue]={p1:int(v1),p2:int(v2),p3:int(v3)}

for name,sue in sues.items():
    if np.sum([realSue[k]==v for k,v in sue.items()]) == 3:
        print("Task1: Sue ",name)

def compare(k,v):
    if k in ["cats","trees"]:
        return realSue[k]<v
    if k in ["pomeranians","goldfish"]:
        return realSue[k]>v
    return realSue[k]==v

for name,sue in sues.items():
    if np.sum([compare(k,v) for k,v in sue.items()]) == 3:
        print("Task2: Sue ",name)
