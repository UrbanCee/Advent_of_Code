import re

rex = "(cpy|inc|dec|jnz) ([-a-z0-9]+) *([-a-z0-9]*)"

with open("inputs/day12.txt") as fp:
    cmds=[(cmd,o1,o2) for line in fp.readlines() for cmd,o1,o2 in re.findall(rex,line)]

r={"a":0,"b":0,"c":0,"d":0}

def run():
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
        if cmd=="jnz" and v!=0:
            ip+=int(o2)
        else:
            ip+=1

run()
print("Task1: ",r["a"])

r={"a":0,"b":0,"c":1,"d":0}
run()
print("Task1: ",r["a"])
