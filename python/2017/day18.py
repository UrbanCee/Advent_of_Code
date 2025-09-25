import re
from collections import deque

with open("inputs/day18.txt") as fp:
    commands = [(cmd,a,b) for line in fp.readlines() for cmd,a,b in re.findall(r'(snd|set|add|mul|mod|rcv|jgz) (-?[a-z0-9]*) ?(-?[a-z0-9]*)?',line)]

cmdMap = {"set":lambda x ,y: y, "add": lambda x,y:x+y, "mul": lambda x,y:x*y, "mod": lambda x,y:x%y}

def evalArg(arg:str,r:dict):
    return (int(arg) if arg.lstrip("-").isnumeric() else r.get(arg,0))

def run(pc,r:dict,freq:deque):
    while 0<=pc<len(commands):
        cmd,a,b = commands[pc]
        if cmd in cmdMap:
            r[a]=cmdMap[cmd](evalArg(a,r),evalArg(b,r))
        elif cmd == "snd":
            freq.append(evalArg(a,r))
        elif cmd == "rcv" and r.get(a,0)>0:
            return freq[-1]
        pc += evalArg(b,r) if cmd == "jgz" and evalArg(a,r)>0 else 1


print("Task 1:",run(0,{},deque()))

