with open("inputs/day2.txt","rt") as fp:
    reports = [list(map(int,line.split())) for line in fp.readlines()]
   
def isSafe(report):
    dir=0;
    for i in range(len(report)-1):
        diff=report[i]-report[i+1]
        if (diff==0):
            return False
        currdir=diff/abs(diff)
        if (dir==0):
            dir=currdir
        else:
            if (dir!=currdir): 
                return False
        if ((abs(diff) <1) or (abs(diff) >3)):
            return False
    return True
    
safecount = 0
safecount_1 = 0
for report in reports:
    if (isSafe(report)):
        safecount+=1
        continue
    else:
        for i in range(len(report)):
            reducedRep = report.copy()
            reducedRep.pop(i)
            if (isSafe(reducedRep)):
                safecount_1+=1
                break
        
        
        
print("Task1: ",safecount)
print("Task2: ",safecount+safecount_1)