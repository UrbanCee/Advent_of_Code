from itertools import groupby

import re

extractRex = re.compile(r'(\d+)[^0-9]+(\d+)[^0-9]+(\d+)[^0-9]+(\d+)')

with open("inputs/day16.txt") as fp:
    commandListStrings=[list(l) for tf,l in groupby([line.strip() for line in fp.readlines()],key=lambda k: k=="") if not tf]
    regList=commandListStrings.pop()

#format: (op,a,b,out),(b0,b1,b2,b3),(a0,a1,a2,a3) 
commands = []
for entry in commandListStrings:
    for op,a,b,out in extractRex.findall(entry[1]):
        opCode=(int(op),int(a),int(b),int(out))
    for b0,b1,b2,b3 in extractRex.findall(entry[0]):
        before=(int(b0),int(b1),int(b2),int(b3))
    for a0,a1,a2,a3 in extractRex.findall(entry[2]):
        after=(int(a0),int(a1),int(a2),int(a3))
    commands.append((opCode,before,after))

def calc(opCode,rIn):
    op,a,b,c = opCode
    r = list(rIn)
    match op:
        case 0: r[c] = r[a] + r[b]
        case 1: r[c] = r[a] + b
        case 2: r[c] = r[a] * r[b]
        case 3: r[c] = r[a] * b
        case 4: r[c] = r[a] & r[b]
        case 5: r[c] = r[a] & b
        case 6: r[c] = r[a] | r[b]
        case 7: r[c] = r[a] | b
        case 8: r[c] = r[a]
        case 9: r[c] = a
        case 10: r[c] = 1 if a > r[b] else 0
        case 11: r[c] = 1 if r[a] > b else 0
        case 12: r[c] = 1 if r[a] > r[b] else 0
        case 13: r[c] = 1 if a == r[b] else 0
        case 14: r[c] = 1 if r[a] == b else 0
        case 15: r[c] = 1 if r[a] == r[b] else 0
    return tuple(r)

def overrideOpCode(opCode,rIn,override):
    op,a,b,c = opCode
    return calc((override,a,b,c),rIn)

threeCorr = 0
opCodeRemap = {}
for (opCode,before,after) in commands:
    correctNum = sum([after==overrideOpCode(opCode,before,i) for i in range(16)])
    if correctNum>=3:
        threeCorr+=1
    if correctNum==1:
        print(opCode)
        opCodeRemap[opCode[0]]=sum([i if after==overrideOpCode(opCode,before,i) else 0 for i in range(16)])

print(opCodeRemap)
print("Task 1:",threeCorr)
    
