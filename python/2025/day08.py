import re
from size import *
from functools import reduce
import operator
with open("inputs/day08.txt") as fp:
    points = [(int(x),int(y),int(z)) for x,y,z in re.findall(r'(\d+),(\d+),(\d+)',fp.read())]

distances = sorted([(v3Len(v3Sub(points[i],points[j])),i,j) for i in range(len(points)) for j in range(i+1,len(points))],key=lambda x:x[0])
circuits = []
connected = set()

for i,(d,a,b) in enumerate(distances):
    circsContAB = [i for i,c in enumerate(circuits) if a in c or b in c]
    if len(circsContAB)==0:circuits.append({a,b})
    if len(circsContAB)==1:circuits[circsContAB[0]]=circuits[circsContAB[0]].union({a,b})
    if len(circsContAB)==2:
        ca,cb=circuits[circsContAB[0]],circuits[circsContAB[1]]
        circuits.remove(ca)
        circuits.remove(cb)
        circuits.append(ca.union(cb))
    if i==999: print("Task 1:",reduce(lambda p,v: p*len(v),sorted(circuits,key=lambda x:-len(x))[:3],1))
    connected=connected.union({a,b})
    if len(connected)==len(points):
        print("Task 2:",points[a][0]*points[b][0])
        break




