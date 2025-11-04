from collections import deque

def manDist4(a,b):
    return sum([abs(a[i]-b[i]) for i in range(len(a))])

with open("inputs/day25.txt") as fp:
    points = [tuple(map(int, line.strip().split(","))) for line in fp.readlines()]

proxymap = {i:[j for j in range(len(points)) if i != j and manDist4(points[i],points[j]) <=3 ] for i in range(len(points))}

processed = set()
constellations = list()
for i in range(len(points)):
    if i in processed: continue
    constellation = {i}
    q = deque()
    q.extend(proxymap[i])
    while len(q)>0:
        p = q.pop()
        constellation.add(p)
        q.extend(p1 for p1 in proxymap[p] if p1 not in constellation)
    constellations.append(constellation)
    processed = processed | constellation

print("Task 1:",len(constellations))
