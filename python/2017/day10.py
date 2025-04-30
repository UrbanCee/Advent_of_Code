import re
rex=re.compile(r'([0-9]+)')
with open("inputs/day10.txt") as fp:
    nmbrs=[int(num) for num in rex.findall(fp.read().strip())]

numberList = range(256)
pos=0
skipSize=0

for length in nmbrs:
    numberList=list(numberList[length:])+list(reversed(numberList[:length]))
    numberList=numberList[skipSize:]+numberList[:skipSize]
    pos=(pos+length+skipSize)%len(numberList)
    skipSize+=1

numberList=numberList[len(numberList)-pos:]+numberList[:len(numberList)-pos]
print("Task 1:",numberList[0]*numberList[1])
