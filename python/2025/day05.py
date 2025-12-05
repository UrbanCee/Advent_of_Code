import re
with open("inputs/day05.txt") as fp:
    input = fp.readlines()
    ranges = list(sorted([(int(a),int(b)) for line in input for a,b in re.findall(r"(\d+)\-(\d+)",line)],key= lambda a:a[0]))

print("Task 1:",sum(sum(i>=a and i<=b for a,b in ranges)>0 for i in [int(i) for line in input for i in re.findall(r"^(\d+)\r?\n",line)]))

def inInt(v:int,a:tuple[int,int]):return v>=a[0] and v<=a[1]
rangeUnion,currentRange = [],ranges[0]
for range in ranges:
    if inInt(range[0],currentRange):
        currentRange=(currentRange[0],max(currentRange[1],range[1]))
    else:
        rangeUnion.append(currentRange)
        currentRange=range
rangeUnion.append(currentRange)

print("Task 2:",sum(b-a+1 for a,b in rangeUnion))    

