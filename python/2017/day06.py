import re
with open("inputs/day06.txt") as fp:
    banks=[int(x) for x in re.findall("(\d+)",fp.read().strip())]

def run():
    savedStates=set()
    while "".join([f"{x:02}" for x in banks]) not in savedStates:
        savedStates.add("".join([f"{x:02}" for x in banks]))
        maxValue=max(banks)
        startIndex=banks.index(maxValue)
        banks[startIndex]=0
        for i in range(1,maxValue+1):
            banks[(startIndex+i)%len(banks)]+=1
    return len(savedStates)
print("Task1: ",run())
print("Task2: ",run())
