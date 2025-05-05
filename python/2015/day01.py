with open("inputs/day01.txt") as fp:
    line=fp.read()

print("Task1: ",line.count("(")-line.count(")"))

currentIndex=0
currentLevel=0
while currentLevel>=0:
    currentLevel+= 1 if line[currentIndex]=="(" else -1
    currentIndex+=1
print("Task2: ",currentIndex)