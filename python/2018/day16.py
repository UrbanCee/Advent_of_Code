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
program=[(int(op),int(a),int(b),int(c)) for reg in regList for op,a,b,c in extractRex.findall(reg)]

def calc(opCode,rIn):
    op,a,b,c = opCode
    r = list(rIn)
    match op:
        case 0: r[c] = r[a] + r[b]                  #addr 
        case 1: r[c] = r[a] + b                     #addi
        case 2: r[c] = r[a] * r[b]                  #mulr
        case 3: r[c] = r[a] * b                     #muli
        case 4: r[c] = r[a] & r[b]                  #bandr
        case 5: r[c] = r[a] & b                     #bandi
        case 6: r[c] = r[a] | r[b]                  #borr
        case 7: r[c] = r[a] | b                     #borri
        case 8: r[c] = r[a]                         #setr
        case 9: r[c] = a                            #seti
        case 10: r[c] = 1 if a > r[b] else 0        #gtir
        case 11: r[c] = 1 if r[a] > b else 0        #gtri
        case 12: r[c] = 1 if r[a] > r[b] else 0     #gtrr
        case 13: r[c] = 1 if a == r[b] else 0       #eqir    
        case 14: r[c] = 1 if r[a] == b else 0       #eqri
        case 15: r[c] = 1 if r[a] == r[b] else 0    #eqrr
    return tuple(r)

def overrideOpCode(opCode,rIn,override):
    _,a,b,c = opCode
    return calc((override,a,b,c),rIn)

def command2PossibleCommands(opCode,before,after,opCodeRemap : dict=dict()):
    return [opCode[0]]+[i for i in range(16) if overrideOpCode(opCode,before,i)==after if i not in opCodeRemap.values()]

print("Task 1:",sum([len(command2PossibleCommands(opCode,before,after))>3 for (opCode,before,after) in commands ]))

opCodeRemap = {}
while len(opCodeRemap)<16:
    commandSet = {tuple(command2PossibleCommands(opCode,before,after,opCodeRemap)) for (opCode,before,after) in commands if opCode[0] not in opCodeRemap}
    for e in commandSet:
        if len(e)<=2:
            opCodeRemap[e[0]]=e[0] if len(e)==1 else e[1]
            break

r=(0,0,0,0)
for cmd in program:
    r=overrideOpCode(cmd,r,opCodeRemap[cmd[0]])
print("Task 2:",r[0])
