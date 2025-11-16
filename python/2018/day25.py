from collections import deque

def manDist4(a,b):
    return sum([abs(ai-b[i]) for i,ai in enumerate(a)])

with open("inputs/day25.txt") as fp:
    points = [tuple(map(int, line.strip().split(","))) for line in fp.readlines()]

proxymap = {i:[j for j,pj in enumerate(points) if i != j and manDist4(pi,pj) <=3 ] for i,pi in enumerate(points)}

processed = set()
constellations = list()
for i,_ in enumerate(points):
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
