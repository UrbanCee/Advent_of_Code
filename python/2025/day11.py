import re
with open("inputs/day11.txt") as fp:
    connections = {node:{con for con in line.strip().split()} for node,line in re.findall("([a-z]+):([a-z ]+)",fp.read())}

callCache = dict()
def findPaths(node:str,target:str,visited:set[str]):
    if target in connections[node]: return 1
    if node+target not in callCache:
        callCache[node+target]=sum(findPaths(nextNode,target,visited.union({node})) for nextNode in connections[node] if nextNode not in visited and nextNode!="out")
    return callCache[node+target]

print("Task 1:",findPaths("you","out",set()))
if (findPaths("dac","fft",set())==0):
    print("Task 2:",findPaths("svr","fft",set())*findPaths("fft","dac",set())*findPaths("dac","out",set()))
else:
    print("Task 2:",findPaths("svr","dac",set())*findPaths("dac","fft",set())*findPaths("fft","out",set()))
