import re
with open("inputs/day07.txt") as fp:
    instr = [(req,proc) for line in fp.readlines() for req,proc in re.compile(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.').findall(line)]

def create_dependencies():
    dep = dict()
    for req,proc in instr:
        dependson = dep.get(proc,set())
        dependson.add(req)
        dep[proc]=dependson
    return ({step for pair in instr for step in pair}, dep)

def remove_item(reqSteps,dependencies,done):
    newDic=dict()
    for proc,rec in dependencies.items():
        if done in rec:
            rec.remove(done)
        if (len(rec)>0):
            newDic[proc]=rec
    reqSteps.remove(done)
    return (reqSteps,newDic)


reqSteps,dependencies = create_dependencies()
solution1 = ""
while len(reqSteps) > 0:
    print(reqSteps,dependencies)
    newStep=sorted([step for step in reqSteps if step not in dependencies.keys()])[0]
    solution1+=newStep
    reqSteps,dependencies=remove_item(reqSteps,dependencies,newStep)

print("Task1: ",solution1)


reqSteps,dependencies = create_dependencies()
time = 0
workers={}
while len(reqSteps) > 0:
    newSteps=sorted([step for step in reqSteps if step not in dependencies.keys() and step not in workers])
    while len(newSteps)>0 and len(workers)<5:
        currentStep=newSteps.pop(0)
        workers[currentStep]=time+61+ord(currentStep)-ord('A')
    nextDone=min(workers,key=lambda w: workers[w])
    time=workers[nextDone]
    reqSteps,dependencies=remove_item(reqSteps,dependencies,nextDone)
    workers.pop(nextDone)


print("Task2: ",time)
    