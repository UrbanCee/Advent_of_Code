import re
rex=re.compile(r'Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).')

def run(discList,time = 0):
    while not sum([(discs[i][1]+i+1+time)%discs[i][0] for i in range(len(discs))])==0:
        time+=1
    return time

with open("inputs/day15.txt") as fp:
    discs=[(int(mod),int(curr)) for line in fp.readlines() for num,mod,time,curr in rex.findall(line)]

print("Task1: ",run(discs))
discs.append((11,0))
print("Task2: ",run(discs))
