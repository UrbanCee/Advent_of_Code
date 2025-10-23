import re
def addPadding(str):
    return "..."+str.strip(".")+"..."
markZeroPos={"#":"X",".":"x"}
with open("inputs/day12.txt") as fp:
    current = fp.readline().strip().strip("initial state: ")
    current = addPadding(markZeroPos[current[0]]+current[1:])
    print(current)
    rules = {key:value for line in fp.readlines() for key,value in re.findall(r'([.#]+) => ([.#])',line) }
def applyRule(str:str):
    strC=str.replace("X","#").replace("x",".")
    return rules[strC] if str[2]!="x" and str[2]!="X" else markZeroPos[rules[strC]]
def nextStep(str):
    return addPadding("".join([ applyRule(str[i:i+5]) for i in range(len(str)-4)]))
for i in range(20):
    current=nextStep(current)
startIndex=current.index("x") if "x" in current else current.index("X")
print("Task1: ",sum([(current[i]=="#" or current[i]=="X")*(i-startIndex) for i in range(len(current))]))
for i in range(979):
    current=nextStep(current)
currentSum=sum([(current[i]=="#" or current[i]=="X")*(i-startIndex) for i in range(len(current))])
current=nextStep(current)
difference=sum([(current[i]=="#" or current[i]=="X")*(i-startIndex) for i in range(len(current))])-currentSum
print("Task2: ",sum([(current[i]=="#" or current[i]=="X")*(i-startIndex) for i in range(len(current))])+(50000000000-1000)*difference)
