with open("inputs/day08.txt") as fp:
    data=[int(x) for x in fp.read().strip().split(" ")]

#data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

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
    childrenValues = []
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
        children.append(child)
        childPos = child.next
    metaData = data[childPos:childPos+metaNum]
    metaCount += sum(metaData)
    if len(children)==0:
        value=sum(metaData)
    else:
        value=sum([children[index-1].value for index in metaData if index-1<len(children)])
    return node(startPos,childPos+metaNum,children,data[childPos:childPos+metaNum],value)

basenode=parse_node(0)
print("Task 1:",metaCount)
print("Task 2:",basenode.value)


