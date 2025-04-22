import re

exprIn = ["^([a-z]+)\\[","\\]([a-z]+)$","\\]([a-z]+)\\["]
exprOut = "\\[([a-z]+)\\]"

def TSL(s):
    for i in range(len(s)-3):
        if s[i]==s[i+3] and s[i+1]==s[i+2] and s[i]!=s[i+1]:
            return True
    return False

def ABAs(s):
    babs=[]
    for i in range(len(s)-2):
        if s[i]==s[i+2] and s[i]!=s[i+1]:
            babs.append(s[i+1]+s[i]+s[i+1])
    return babs


TSLcount=0
SSLcount=0


with open("inputs/day07.txt") as fp:
    for line in fp.readlines():
        isTSL=False
        isSSL=False
        babs=[]
        for eIn in exprIn:
            for addr in re.findall(eIn,line):
                isTSL=isTSL or TSL(addr)
                babs.extend(ABAs(addr))
        for addr in re.findall(exprOut,line):
            isTSL=isTSL and not TSL(addr)
            for bab in babs:
                isSSL = isSSL or (bab in addr)
        if isTSL: TSLcount+=1
        if isSSL: SSLcount+=1

print("Task1: ",TSLcount)
print("Task2: ",SSLcount)

