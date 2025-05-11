from itertools import combinations
from size import *
with open("inputs/day02.txt") as fp:
    IDs = [line for line in map(str.strip,fp.readlines())]

def returnCommonChars(s):
    return "".join([s[0][i] for i in range(len(s[0])) if s[0][i]==s[1][i]])

print("Task1 :", sum([2 in charInv(line).values() for line in IDs])*sum([3 in charInv(line).values() for line in IDs]))
print("Task2 :", returnCommonChars([(s1,s2) for s1,s2 in combinations(IDs,2) if sum([s1[i]!=s2[i] for i in range(len(s1))])==1][0]))
