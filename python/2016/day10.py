import re

botExpr = "bot (\\d+) gives low to (bot|output) (\\d+) and high to (bot|output) (\\d+)"
inputExpr = "value (\\d+) goes to bot (\\d+)"

bots = {}
outputs = {}
with open("inputs/day10.txt") as fp: cmds=fp.read().strip()

def addValueTo(dest,b,v):
    if dest=="bot":
        ld1,l1,hd1,h1,vs=bots[b]
        bots[b]=(ld1,l1,hd1,h1,vs+[v])
    else:
        if b not in outputs.keys(): outputs[b] = [v]
        else: outputs[b] = outputs[b]+[v]


for b,ld1,l1,hd1,h1 in re.findall(botExpr,cmds):
    bots[b]=(ld1,l1,hd1,h1,[])
for v,b in re.findall(inputExpr,cmds):
    addValueTo("bot",b,int(v))

outputs = {}

botsProcessed = set()
while(len(botsProcessed)<len(bots)):
    for b,bv in [(b,bv) for b,bv in bots.items() if len(bv[4])==2 and b not in botsProcessed]:
        ld1,l1,hd1,h1,vs=bv
        vs = sorted(vs)
        if vs==[17,61]: print("Task1:",b)
        addValueTo(ld1,l1,vs[0])
        addValueTo(hd1,h1,vs[1])
        botsProcessed.add(b)

print("Task2:",outputs["0"][0]*outputs["1"][0]*outputs["2"][0])