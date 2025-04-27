import re

rex = "(cpy|inc|dec|jnz|out) ([-a-z0-9]+) *([-a-z0-9]*)"

with open("inputs/day25.txt") as fp:
    cmds=[(cmd,o1,o2) for line in fp.readlines() for cmd,o1,o2 in re.findall(rex,line)]

def run(r):
    lastOut=-1
    ip = 0
    while(ip<len(cmds)):
        cmd,o1,o2 = cmds[ip]
        if o1 in r.keys():
            v=r[o1]
        else:
            v=int(o1)
        if cmd=="cpy":
            r[o2]=v
        elif cmd=="inc":
            r[o1]=r[o1]+1
        elif cmd=="dec":
            r[o1]=r[o1]-1
        elif cmd=="out":
            if lastOut==-1:lastOut=v
            else:
                if v in [0,1] and v+lastOut==1:
                    lastOut=v
                else:
                    return r
        if cmd=="jnz" and v!=0:
            ip+=int(o2)
        else:
            ip+=1
    return r

for a in range(100000):
    print(a)
    run({"a":a,"b":0,"c":0,"d":0})