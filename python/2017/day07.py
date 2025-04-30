import re
towerPat=re.compile(r'([a-z]+) \((\d+)\) *\-*>* *([a-z ,]*)')
connectionsPat=re.compile(r'([a-z]+)')
with open("inputs/day07.txt") as fp:
    nodes={name:(int(weight),"",[child for child in connectionsPat.findall(children)]) for line in fp.readlines() for name,weight,children in towerPat.findall(line)}


for name,(weight,parent,children) in nodes.items():
    for child in children:
        childWeight,parent,childChildren=nodes[child]
        nodes[child]=(childWeight,name,childChildren)
for name,(weight,parent,children) in nodes.items():
    if parent=="":
        towerbase=name
print("Task1: ",towerbase)

def getWeight(nodeName):
    weight,parent,children = nodes[nodeName]
    childrenWeights=[getWeight(c) for c in children]
    if (len(childrenWeights)>1):
        if (sum([childrenWeights[0]!=w for w in childrenWeights])>0):
            print("unbalanced in node",nodeName,"whith children",children,"with weights",childrenWeights)
            childrenisolatedWeights=[nodes[c][0] for c in children]
            print(childrenWeights)
            print(childrenisolatedWeights)
        
            
    return weight+sum(childrenWeights)

getWeight(towerbase)
    
        
