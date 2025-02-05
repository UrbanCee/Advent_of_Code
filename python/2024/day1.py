
list 

with open("inputs/day1.txt","rt") as fp:
    lines = [list(map(int,line.split())) for line in fp.readlines()]

left = [x[0] for x in lines]
right = [x[1] for x in lines]

print("Task1: ",sum([abs(x-y) for x,y in zip(sorted(left),sorted(right))]))
print("Task2: ",sum([x*right.count(x) for x in left]))


  
        
