import re
expr = "(\\d+) +(\\d+) +(\\d+)"
nonTriangles=0
triangles=0
nmbrs = []
with open("inputs/day03.txt") as fp:
    for line in fp.readlines():
        for numbers in [[int(v1),int(v2),int(v3)] for v1,v2,v3 in re.findall(expr,line)]:
            nmbrs.append(numbers)
        for lengths in [sorted([int(v1),int(v2),int(v3)]) for v1,v2,v3 in re.findall(expr,line)]:
            if (lengths[0]+lengths[1]>lengths[2]):
                nonTriangles+=1

for column in range(3):
    for row in range(0,len(nmbrs),3):
        sortedNums=sorted([nmbrs[row][column],nmbrs[row+1][column],nmbrs[row+2][column]])
        if sortedNums[0]+sortedNums[1]>sortedNums[2]:
            triangles+=1


            
print("Task1: ",nonTriangles)
print("Task2: ",triangles)

