with open("inputs/day08.txt") as fp:
    data=[int(x) for x in fp.read().strip().split(" ")]

data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

class node:
    def __init__(self,pos,next,children,meta,value):
        self.pos=pos
        self.next=next
        self.children=children
        self.meta=meta
        self.value=value
    pos = 0
    next = 0
    children = []
    meta = []
    value = 0

metaCount = 0

def parse_node(startPos):
    global metaCount
    childPos=startPos+2
    chNum,metaNum = data[startPos:childPos]
    children = []
    for i in range(0,chNum):
        child = parse_node(childPos)
        children.append(childPos)
        childPos = child.next
    metaCount += sum(data[childPos:childPos+metaNum])
    return node(startPos,childPos+metaNum,children,data[childPos:childPos+metaNum],0)

print(parse_node(0).children)
print("Task 1:",metaCount)


