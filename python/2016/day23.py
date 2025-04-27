import re

rexPat = re.compile("(cpy|inc|dec|jnz|tgl) ([-a-z0-9]+) *([-a-z0-9]*)")
numRex = re.compile("-*[0-9]+")

with open("inputs/day23.txt") as fp:
    prog=[(cmd,o1,o2) for line in fp.readlines() for cmd,o1,o2 in rexPat.findall(line)]

multcode = [("cpy","0","a"),("cpy","b","c"),("inc","a",""),("dec","c",""),("jnz","c","-2"),("dec","d",""),("jnz","d","-5")]

def printCode(cmds,r,ip):
    print("-----------------begin----------------")
    print(f"Registers: a={r["a"]}  b={r["b"]}  c={r["c"]}  d={r["d"]}")
    for i in range(len(cmds)):
        pos="->" if ip==i else "  "
        print(f"{pos}{cmds[i][0]} {cmds[i][1]} {cmds[i][2]}")
    print("-----------------end------------------")
    

def run(r,cmds):
    ip = 0
    while(ip<len(cmds) and ip>=0):
        #printCode(cmds,r,ip)
        cmd,o1,o2 = cmds[ip]
        if o1 in r.keys():
            v=r[o1]
        else:
            v=int(o1)
        if cmd=="cpy" and o2 in r.keys():
            r[o2]=v
            if cmds[ip]==multcode[0]:
                if sum([multcode[i]==cmds[ip+i] for i in range(1,len(multcode))])==6:
                    r["a"]=r["b"]*r["d"]
                    r["c"],r["d"]=0,0
                    ip+=7
                    continue
        elif cmd=="inc" and o1 in r.keys():
            r[o1]=r[o1]+1
        elif cmd=="dec" and o1 in r.keys():
            r[o1]=r[o1]-1
        elif cmd=="tgl":
            pos=ip+v
            if pos>=0 and pos<len(cmds):
                target=cmds[pos]
                if target[0]=="inc":
                    cmds[pos]=("dec",target[1],target[2])
                elif target[0]=="dec" or target[0]=="tgl":
                    cmds[pos]=("inc",target[1],target[2])
                elif target[0]=="jnz":
                    cmds[pos]=("cpy",target[1],target[2])
                elif target[0]=="cpy":
                    cmds[pos]=("jnz",target[1],target[2])
        if cmd=="jnz" and v!=0:
            if o2 in r.keys():
                ip+=r[o2]
            if numRex.search(o2):
                ip+=int(o2)
        else:
            ip+=1
    return r

#n!+7614
print("Task1: ",run({"a":7,"b":0,"c":0,"d":0},list(prog))["a"])
print("Task2: ",run({"a":12,"b":0,"c":0,"d":0},list(prog))["a"])

