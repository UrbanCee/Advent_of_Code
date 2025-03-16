from size import *
from queue import PriorityQueue

f1="inputs/day16_training_1.txt"
f2="inputs/day16_training_2.txt"
f3="inputs/day16.txt"

with open(f3,"rt") as fp:
    lines = fp.readlines()

playfield = "".join(map(str.strip,lines))
s = mySize(len(lines[0].strip()),len(lines))

def outputPlayfield(field):
    for y in range(s.w):
        print(field[y*s.w:(y+1)*s.w])
    
#outputPlayfield()

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
class Agent:
    invalidated = False
    def __init__(self,pos=0,dir=0,cost=0,visited=set()):
        (self.pos,self.dir,self.cost,self.visited)=(pos,dir,cost,visited)
    def vDir(self):
        return dirs[dir]
    def move(self,dirOffset):
        visited = self.visited.copy()
        visited.add(self.pos)
        turnCost = 0
        if (dirOffset!=0): turnCost=1000
        newDir = (self.dir+dirOffset)%4
        return Agent(s.addVecToInd(self.pos,dirs[newDir]),newDir,self.cost+1+turnCost,visited)
    def __lt__(self,obj):
        return self.cost<obj.cost
    def __str__(self):
        return "at: "+str(s.toVec(self.pos))+" with cost: "+str(self.cost)+" looking: "+str(self.dir)

visited = {}
queue = PriorityQueue()


def moveToNode(currentAgent,newAgents):
    visitedCurrentNode = visited.get(currentAgent.pos,[])
    for agent in newAgents:
        queue.put(agent)
        visitedCurrentNode.append(agent)
    visited[currentAgent.pos]=visitedCurrentNode

currentAgent = Agent(playfield.find("S"),0,0,set())
queue.put(currentAgent)
costFound=-1
while((not queue.empty()) and playfield[currentAgent.pos]!="E"):
    currentAgent = queue.get()
    #print(currentAgent)
    newAgents=[]
    for nextDir in [0,1,3]:
        newAgent=currentAgent.move(nextDir)
        if (playfield[newAgent.pos]!="#"):
            newAgents.append(newAgent)
    if currentAgent.pos in visited:
        collisionAgents=visited[currentAgent.pos]
        for collisionAgent in collisionAgents:
            if (collisionAgent.pos,collisionAgent.dir) in [(collider.pos,collider.dir) for collider in newAgents ]:
                for collider in newAgents:
                    if collider.pos==collisionAgent.pos and collider.dir==collisionAgent.dir: 
                        if collider.cost==collisionAgent.cost:
                            collisionAgent.visited=collisionAgent.visited.union(collider.visited)
                        elif collider.cost<collisionAgent.cost:
                            moveToNode(currentAgent,[collider])
    else:
        moveToNode(currentAgent,newAgents)
visitedPlayfield=str(playfield)
for ind in currentAgent.visited:
    visitedPlayfield=visitedPlayfield[:ind]+"O"+visitedPlayfield[ind+1:]
outputPlayfield(visitedPlayfield)

print("task1:",currentAgent.cost)
print("task2:",len(currentAgent.visited)+1)





