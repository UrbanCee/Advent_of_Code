import re

expr = "([a-z]+)\\[([a-z]+)\\]([a-z]+)"

def TSL(s):
    for i in range(len(s)-3):
        if s[i]==s[i+3] and s[i+1]==s[i+2] and s[i]!=s[i+1]:
            return True
    return False

IPcount=0


with open("inputs/day07.txt") as fp:
    for line in fp.readlines():
        for s1,b,s2 in re.findall(expr,line):
            print(line,s1,s2,b,(TSL(s1) or TSL(s2)) and not TSL(b))
            if (TSL(s1) or TSL(s2)) and not TSL(b):
                IPcount+=1

print("Task1: ",IPcount)

