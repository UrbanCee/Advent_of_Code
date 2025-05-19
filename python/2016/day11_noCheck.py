from itertools import accumulate

print("Task 1:",list(accumulate([(4,0),(5,0),(1,0)],lambda acc,x:(acc[0]+x[0],acc[1]+2*(x[0]+acc[0]-1)-1),initial=(0,0)))[-1][1])
print("Task 2:",list(accumulate([(8,0),(5,0),(1,0)],lambda acc,x:(acc[0]+x[0],acc[1]+2*(x[0]+acc[0]-1)-1),initial=(0,0)))[-1][1])