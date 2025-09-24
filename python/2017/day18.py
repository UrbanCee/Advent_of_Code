import re
from collections import deque

with open("inputs/day18.txt") as fp:
    commands = [(cmd,a,b) for line in fp.readlines() for cmd,a,b in re.findall(r'(snd|set|add|mul|mod|rcv|jgz) (-?[a-z0-9]) ?(-?[a-z0-9])?',line)]

cmdMap = {"set":lambda x ,y: y, "add": lambda x,y:x+y, "mul": lambda x,y:x*y, "mod": lambda x,y:x%y}

def run(pc,r:dict,freq : deque):
    while pc<len(commands) and pc>=0:
        cmd,a,b = commands[pc]
        if a.lstrip("-").isnumeric():
            va=int(a)
        else:
            va=r.get(a,0)
        if b.lstrip("-").isnumeric():
            vb=int(b)
        else:
            vb=r.get(b,0)
        print(r)
        print(cmd,a,b)
        print(a,va,b,vb)
        if cmd in cmdMap:
            r[a]=cmdMap[cmd](va,vb)
        elif cmd == "snd":
            freq.append(va)
            print(va)
        elif cmd == "rcv" and freq[-1]>0:
            return freq[-1]
        if cmd == "jgz" and va>0:
            pc+=vb
        else:
            pc+=1


print("Task 1:",run(0,{},deque()))

