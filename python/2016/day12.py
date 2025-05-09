import re

rex = re.compile(r'(cpy|inc|dec|jnz) ([-a-z0-9]+) *([-a-z0-9]*)')

with open("inputs/day12.txt") as fp:
    cmds=[(cmd,o1,o2) for line in fp.readlines() for cmd,o1,o2 in rex.findall(line)]

def run(r):
    ip = 0
    while(ip<len(cmds)):
        cmd,o1,o2 = cmds[ip]
        v = r[o1] if o1 in r.keys() else int(o1)
        if cmd=="cpy":
            r[o2]=v
        elif cmd in ["inc","dec"]:
            r[o1]=r[o1]+1 if cmd=="inc" else r[o1]-1
        ip+=int(o2) if cmd=="jnz" and v!=0 else 1
    return r

print("Task1: ",run({"a":0,"b":0,"c":0,"d":0})["a"])
print("Task2: ",run({"a":0,"b":0,"c":1,"d":0})["a"])
