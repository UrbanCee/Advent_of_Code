with open("inputs/day05.txt") as fp:
    jumps = [int(line.strip()) for line in fp.readlines()]

def jump(jumps,part=1):
    pos,steps=0,0
    while pos>=0 and pos<len(jumps):
        offset=jumps[pos]
        if (part==1):
            jumps[pos]=offset+1
        else:
            jumps[pos]=offset-1 if offset>=3 else offset+1
        pos+=offset
        steps+=1
    return steps

print("Task1: ",jump(list(jumps)))
print("Task2: ",jump(list(jumps),2))

