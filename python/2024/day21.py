from size import *
from itertools import permutations
with open("inputs/day21_training.txt","rt") as fp:
    codes = [line.strip() for line in fp.readlines()]

alphaNumKeyboard = [["7","8","9"],["4","5","6"],["1","2","3"],["F","0","A"]]
directionalKeyboard = [["F","^","A"],["<","v",">"]]
alphaNumFlat = ["7","8","9","4","5","6","1","2","3","0","A"]
directionalFlat = ["^","A","<","v",">"]
alphaNumMap = {"7":(0,0),"8":(1,0),"9":(2,0),"4":(0,1),"5":(1,1),"6":(2,1),"1":(0,2),"2":(1,2),"3":(2,2),"F":(0,3),"0":(1,3),"A":(2,3)}
pos2AlphaNum = {(0,0):"7",(1,0):"8",(2,0):"9",(0,1):"4",(1,1):"5",(2,1):"6",(0,2):"1",(1,2):"2",(2,2):"3",(0,3):"F",(1,3):"0",(2,3):"A"}
directionalMap = {"F":(0,0),"^":(1,0),"A":(2,0),"<":(0,1),"v":(1,1),">":(2,1)}
pos2Dir = {(0,0):"F",(1,0):"^",(2,0):"A",(0,1):"<",(1,1):"v",(2,1):">"}
allAlphaNumPairs =[alphaNumFlat[i]+alphaNumFlat[j] for i in range(len(alphaNumFlat)) for j in range(len(alphaNumFlat))]
allDirectionalPairs =[directionalFlat[i]+directionalFlat[j] for i in range(len(directionalFlat)) for j in range(len(directionalFlat))]
deltaMap = {">":(1,0),"<":(-1,0),"^":(0,-1),"v":(0,1)}

def allowedCombo(start,combostring,pos2ButtonMap):
    pos = start
    for cmd in combostring:
        if cmd=="A": return True
        pos = vAdd(pos,deltaMap[cmd])
        if (pos2ButtonMap[pos]=="F"): return False


def pair2CodeArray(pair,buttonMap,pos2ButtonMap):
    start = buttonMap[pair[0]]
    end = buttonMap[pair[1]]
    delta = vSub(end,start)
    totalsteps=abs(delta[0])+abs(delta[1])
    updownChar="^"
    if (delta[1]>0): updownChar="v"
    leftRightChar="<"
    if (delta[0]>0): leftRightChar=">"
    baseString = leftRightChar*abs(delta[0])+updownChar*abs(delta[1])
    validCodes = []
    for codeSet in set(permutations(baseString)):
        code="".join(codeSet)+"A"
        if allowedCombo(start,code,pos2ButtonMap):
            validCodes.append(code)
    return validCodes

alphaPairArrays = {pair: pair2CodeArray(pair,alphaNumMap,pos2AlphaNum) for pair in allAlphaNumPairs}
dirMapArrays = {pair:pair2CodeArray(pair,directionalMap,pos2Dir) for pair in allDirectionalPairs}

for (pair,dirMap) in dirMapArrays.items():
    if len(dirMap)>1:
        for dir in dirMap:
            print(pair,dir,":")






