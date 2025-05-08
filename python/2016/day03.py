import re
expr = re.compile(r"(\d+) +(\d+) +(\d+)")
def isTriangle(t): return t[0]+t[1]>t[2]    

with open("inputs/day03.txt") as fp:
    numbers = [(int(v1),int(v2),int(v3)) for line in fp.readlines() for v1,v2,v3 in expr.findall(line)]

print("Task1: ",sum([isTriangle(sorted(t)) for t in numbers]))
print("Task2: ",sum([isTriangle(sorted([numbers[row][column],numbers[row+1][column],numbers[row+2][column]])) for row in range(0,len(numbers),3) for column in range(3)]))


