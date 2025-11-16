from itertools import combinations
from size import *
with open("inputs/day02.txt") as fp:
    IDs = [line for line in map(str.strip,fp.readlines())]

def returnCommonChars(s):
    return "".join([si for i,si in enumerate(s[0]) if si==s[1][i]])

print("Task1 :", sum([2 in charInv(line).values() for line in IDs])*sum([3 in charInv(line).values() for line in IDs]))
print("Task2 :", returnCommonChars([(s1,s2) for s1,s2 in combinations(IDs,2) if sum([s1i!=s2[i] for i,s1i in enumerate(s1)])==1][0]))
