edges = []
with open("inputs/day23_training.txt","rt") as fp:
    for line in fp.readlines():
        if "-" in line:
            edges.append(list(line.strip().split("-")))
nodes = {}
def addnode(l,r):
    ele=nodes.get(l,set())
    ele.add(r)
    nodes[l]=ele
for (l,r) in edges:
    addnode(l,r)
    addnode(r,l)

nodeArray = list(nodes.keys())

def printmatrix(adjMat):
    header = "    "
    for node in nodeArray:
        header+=" "+node+" "
    print(header)
    for index in range(len(adjMat)):
        line = " " + nodeArray[index] + " "
        for entry in adjMat[index]:
            line+=f" {entry:2} "
        print(line)

adjMat = []
for node in nodeArray:
    adjMat.append([1 if node in nodes[con] else 0 for con in nodeArray])

aaMat = []
for aai in range(len(nodeArray)):
    aaLine = []
    for aaj in range(len(nodeArray)):
        entry=0
        for k in range(len(nodeArray)):
            entry+=adjMat[aai][k]*adjMat[k][aaj]
        aaLine.append(entry)
    aaMat.append(aaLine)


printmatrix(adjMat)
printmatrix(aaMat)


    
