import re
from itertools import combinations as cm
numPat=re.compile(r'(\d+)')
with open("inputs/day02.txt") as fp:
    numbers=[[int(n) for n in numPat.findall(line)] for line in fp.readlines()]

print("Task 1:",sum([ max(line)-min(line) for line in numbers ]))
print("Task 2:",sum([ max(v1,v2)//min(v1,v2) for line in numbers for v1,v2 in cm(line,2) if max(v1,v2)%min(v1,v2)==0]))