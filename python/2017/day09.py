from collections import deque as dq
import re
with open("inputs/day09.txt") as fp:
    stream=dq(fp.read().strip())
removeExcl=[]
while len(stream) > 0:
    next=stream.popleft()
    if next=="!":
        stream.popleft()
    else:
        removeExcl.append(next)
print("Task2: ",sum([len(garb)-2 for garb in re.findall(r'<[^>]*?>',"".join(removeExcl))]))
clean=dq(re.sub(r'<[^>]*?>',"","".join(removeExcl)))
currentLevel=0
totalSum=0
while len(clean)>0:
    next=clean.popleft()
    if next=="{":
        currentLevel+=1
    if next=="}":
        totalSum+=currentLevel
        currentLevel-=1

print("Task1: ",totalSum)