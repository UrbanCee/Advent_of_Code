from itertools import groupby
l,h = 367479,893698

def check_task1(string):
    return min([ ord(string[i+1])-ord(string[i]) for i in range(len(string)-1)])>=0 and max([string.count(ch) for ch in string])>1
def check_task2(string):
    return min([ ord(string[i+1])-ord(string[i]) for i in range(len(string)-1)])>=0 and sum([len(list(g))==2 for _,g in groupby(string)])>0

print("Task 1:",sum([check_task1(str(i)) for i in range(l,h+1)]))
print("Task 2:",sum([check_task2(str(i)) for i in range(l,h+1)]))

