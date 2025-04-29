import re
from queue import PriorityQueue as PQ

subsRe = "^([A-Za-z]+) => ([A-Za-z]+)$"
keyRe = "^([A-Za-z0-9]+)$"

subs=[]

with open("inputs/day19.txt") as fp:
    for line in fp.readlines():
        if len(line)==0:
            continue
        for src,dest in re.findall(subsRe,line.strip()):
            subs.append((src,dest))
        for k in re.findall(keyRe,line.strip()):
            molecule=k


def positionsOfElements(string:str,el):
    return [i for i in range(len(string)) if string.startswith(el,i)]
def replaceAtPos(string,pos,lenEl,subs):
    return string[:pos]+subs+string[pos+lenEl:]
newMolecules=set()
for el,sub in subs:
    for pos in positionsOfElements(molecule,el):
        newMolecules.add(replaceAtPos(molecule,pos,len(el),sub))
print("Task1: ",len(newMolecules))

elems=re.compile(r'[A-Z][a-z]?')
print("Task2: ",len(elems.findall(molecule))-molecule.count("Ar")*2-molecule.count("Y")*2-1)