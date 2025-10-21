from size import *
import re
pattern = re.compile(r'\/dev\/grid\/node-x(\d+)-y(\d+)\s*(\d+)T\s*(\d+)T\s*(\d+)T\s*(\d+)%')
nodes = {}
with open("inputs/day22.txt") as fp:
    nodes = {(x,y):(size,used,free,pz) for x,y,size,used,free,pz in [(int(x),int(y),int(size),int(used),int(free),int(pz)) for line in fp.readlines() for x,y,size,used,free,pz in pattern.findall(line)]}
    s = mySize(max(nodes.keys(),key=lambda x:x[0])[0]+1,max(nodes.keys(),key=lambda x:x[1])[1]+1)

print("Task1: ",sum([a!=b and nodes[a][1]>0 and nodes[a][1]<=nodes[b][2] for a in nodes.keys() for b in nodes.keys()]))
targetsize=nodes[(s.w-1,0)][1]
sizematrix=[nodes[(x,y)][1] for y in range(s.h) for x in range(s.w)]
s.print("".join(["#" if value>3*targetsize else ("_" if value==0 else ".") for value in sizematrix]))