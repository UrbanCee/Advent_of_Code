import re
import itertools as it
import numpy as np

expr = "([A-Za-z]+) to ([A-Za-z]+) = (\\d+)"
dists = {}
locations = set()

with open("inputs/day09.txt") as fp:
    for line in fp.readlines():
        for (ori,dest,dist) in re.findall(expr,line):
            dists[ori+dest]=int(dist)
            dists[dest+ori]=int(dist)
            locations.add(dest)
            locations.add(ori)

distances = [np.sum([dists[move] for move in [entry[a]+entry[a+1] for a in range(len(entry)-1)]]) for entry in it.permutations(locations)]
print("Task1: ",np.min( distances ))
print("Task2: ",np.max( distances ))
