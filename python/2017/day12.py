import re
from collections import deque
rex = re.compile(r'(\d+) <\-> (.*)')
nums = re.compile(r'(\d+)')
with open("inputs/day12.txt") as fp:
    nodeCon={int(n):[int(t) for t in nums.findall(targets)] for line in fp.readlines() for n,targets in rex.findall(line)}

visitedNodes = set()

def calcGroup(initialElem):
    elemsInThisGroup = set([initialElem])
    nodeQueue = deque(nodeCon[initialElem])
    while len(nodeQueue)>0:
        nextNode=nodeQueue.popleft()
        visitedNodes.add(nextNode)
        elemsInThisGroup.add(nextNode)
        nodeQueue.extend([n for n in nodeCon[nextNode] if n not in visitedNodes])
    return elemsInThisGroup

numOfGroups=1
print("Task1: ",len(calcGroup(0)))
while (len(visitedNodes) < len(nodeCon)):
    calcGroup([p for p in nodeCon.keys() if p not in visitedNodes][0])
    numOfGroups+=1
print("Task2: ",numOfGroups)
