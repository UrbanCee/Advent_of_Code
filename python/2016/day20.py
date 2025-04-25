import re

rex = r'(\d+)\-(\d+)'

with open("inputs/day20.txt") as fp:
    firewall=sorted([(int(lo),int(hi)) for line in fp.readlines() for lo,hi in re.findall(rex,line)])

protectedTo=0
openCount=0
for lo,hi in firewall:
    if lo>protectedTo+1:
        if openCount==0:
            print("Task1: ",protectedTo+1)
        openCount+=lo-protectedTo-1
    protectedTo=max(hi,protectedTo)
print("Task2: ",openCount)
