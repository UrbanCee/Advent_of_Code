import re
from collections import deque

with open("inputs/day18.txt") as fp:
    commands = [(cmd,a,b) for line in fp.readlines() for cmd,a,b in re.findall(r'(snd|set|add|mul|mod|rcv|jgz) (-?[a-z0-9]*) ?(-?[a-z0-9]*)?',line)]

cmdMap = {"set":lambda x ,y: y, "add": lambda x,y:x+y, "mul": lambda x,y:x*y, "mod": lambda x,y:x%y}

def evalArg(arg:str,r:dict):
    return (int(arg) if arg.lstrip("-").isnumeric() else r.get(arg,0))

def run(pc,r:dict,outBuf:deque,inBuf:deque,id,task):
    while 0<=pc[id]<len(commands):
        cmd,a,b = commands[pc[id]]
        if cmd in cmdMap:
            r[a]=cmdMap[cmd](evalArg(a,r),evalArg(b,r))
        elif cmd == "snd":
            outBuf.append(evalArg(a,r))
            if id==1:
                pc[2]+=1
        elif cmd == "rcv":
            if task==1 and r.get(a,0)>0:
                return outBuf[-1]
            if task==2:
                if not inBuf:
                    return 1#program waiting
                r[a]=inBuf.popleft()
        pc[id] += evalArg(b,r) if cmd == "jgz" and evalArg(a,r)>0 else 1
    return 2 #program term

print("Task 1:",run([0],{},deque(),deque(),0,1))

pc, ra, rb, a2b, b2a, state = [0,0,0], {'p':0}, {'p':1}, deque(), deque(), (0,0)
while (state != (2,2)) and not(state[0]==1 and not b2a):#both finished or no now msgs for first program
    state=(run(pc,ra,a2b,b2a,0,2),run(pc,rb,b2a,a2b,1,2))
print("Task 2:",pc[2])

