import re
from collections import deque
rex = re.compile(r'(\d+) <\-> (.*)')
nums = re.compile(r'(\d+)')
with open("inputs/day12.txt") as fp:
    nodeCon={int(n):[int(t) for t in nums.findall(targets)] for line in fp.readlines() for n,targets in rex.findall(line)}

visitedNodes = set([0])
nodeQueue = deque(nodeCon[0])
while len(nodeQueue)>0:
    nextNode=nodeQueue.popleft()
    visitedNodes.add(nextNode)
    nodeQueue.extend([n for n in nodeCon[nextNode] if n not in visitedNodes])
print("Task1: ",len(visitedNodes))

    
    