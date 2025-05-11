import re

with open("inputs/day03.txt") as fp:
    claims=[(int(ID),int(posx),int(posy),int(w),int(h)) for line in fp.readlines() for ID,posx,posy,w,h in re.findall(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)',line)]

def expand(claim):
    return [(x,y) for x in range(claim[1],claim[1]+claim[3]) for y in range(claim[2],claim[2]+claim[4])]

visited = {}
for v in [(x,y) for claim in claims for x,y in expand(claim)]:
    visited[v]=visited.get(v,0)+1

print("Task 1:",sum([v>1 for v in visited.values()]))
print("Task 2:",[claim[0] for claim in claims if sum([visited[p]!=1 for p in expand(claim)])==0])

