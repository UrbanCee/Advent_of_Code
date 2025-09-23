import re

with open("inputs/day13.txt") as fp:
    scanners = {int(r):int(d) for line in fp.readlines() for r,d in re.findall(r'(\d+): (\d+)',line)}

print("Task 1: ",sum([ps*scanners[ps] for ps in range(max(scanners.keys())+1) if ps in scanners and ps%(2*(scanners[ps]-1))==0]))

def caught(delay):
    return len([ps*scanners[ps] for ps in range(max(scanners.keys())+1) if ps in scanners and (ps+delay)%(2*(scanners[ps]-1))==0])>0
safeDelay=0
while caught(safeDelay):
    safeDelay+=1

print("Task 2: ",safeDelay)