with open("inputs/day01.txt") as fp:
    line=fp.read()

up=line.count("(")
down=line.count(")")
print("up:",up,"down:",down,"total:",up-down)

currentIndex=0
currentLevel=0
while currentLevel>=0:
    currentLevel+= 1 if line[currentIndex]=="(" else -1
    currentIndex+=1
print(currentIndex)