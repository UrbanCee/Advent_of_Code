edges = []
with open("inputs/day23.txt","rt") as fp:
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

currentConnList = edges.copy()

countWithT = 0
listlength = 2
while len(currentConnList)>0:
    biggerList = []
    for group in currentConnList:
        inters = nodes[group[0]]
        for node in group:
            inters = inters.intersection(nodes[node])
        for elem in inters:
            if elem not in group:
                newEntry = group.copy()
                newEntry.append(elem)
                if sorted(newEntry) not in biggerList:
                    biggerList.append(sorted(newEntry))

    if (listlength==2):
        for entry in biggerList:
            if "t" in [entry[i][0] for i in range(0,3)]:
                countWithT += 1
    if len(biggerList)==0:
        print("task2:",biggerList)
    listlength+=1
    print(listlength)
    print(biggerList)
    currentConnList=biggerList.copy()

print("task1:",countWithT)
