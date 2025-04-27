import re
numPat=re.compile(r'(\d+)')
with open("inputs/day02.txt") as fp:
    numbers=[[int(n) for n in numPat.findall(line)] for line in fp.readlines()]

print("Task 1:",sum([ max(line)-min(line) for line in numbers ]))