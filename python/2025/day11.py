import re
with open("inputs/day11.txt") as fp:
    connections = {node:{con for con in line.strip().split()} for node,line in re.findall("([a-z]+):([a-z ]+)",fp.read())}

callCache = dict()
def findPaths(node:str,visited:set[str]):
    if node in callCache: return callCache[node]
    if "out" in connections[node]: return 1
    return sum(findPaths(nextNode,visited.union({node})) for nextNode in connections[node] if nextNode not in visited)

print("Task 1:",findPaths("you",set()))
