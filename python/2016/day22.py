import re
pattern = re.compile(r'\/dev\/grid\/node-x(\d+)-y(\d+)\s*(\d+)T\s*(\d+)T\s*(\d+)T\s*(\d+)%')
nodes = {}
with open("inputs/day22.txt") as fp:
    for x,y,size,used,free,pz in [(int(x),int(y),int(size),int(used),int(free),int(pz)) for line in fp.readlines() for x,y,size,used,free,pz in pattern.findall(line)]:
        nodes[(x,y)]=(size,used,free,pz)

print("Task1: ",sum([a!=b and nodes[a][1]>0 and nodes[a][1]<=nodes[b][2] for a in nodes.keys() for b in nodes.keys()]))
