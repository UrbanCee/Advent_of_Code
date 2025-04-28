import re
from  itertools import combinations
wordPat = re.compile(r'([a-z]+)')
with open("inputs/day04.txt") as fp:
    phrases=[[phrase for phrase in wordPat.findall(line)] for line in fp.readlines()]

print("Task 1:",sum([sum([v1==v2 for v1,v2 in combinations(phrase,2)])==0 for phrase in phrases]))
print("Task 2:",sum([sum([sorted(v1)==sorted(v2) for v1,v2 in combinations(phrase,2)])==0 for phrase in phrases]))
