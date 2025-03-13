from size import *

f1="inputs/day20_training.txt"
f2="inputs/day20.txt"

with open(f2,"rt") as fp:
    lines = fp.readlines()

racetrack = "".join(map(str.strip,lines))
s = mySize(len(lines[0].strip()),len(lines))

def manhatten_dist(v:tuple[int,int]):
    return abs(v[0])+abs(v[1])

race_dirs = [(1,0),(0,1),(-1,0),(0,-1)]

#run race without cheating
pos = racetrack.rfind("S")
race = {pos:0}
while(racetrack[pos]!="E"):
    for dir in race_dirs:
        if (s.outOfBoundsPlusOffset(pos,dir)):
            continue
        newpos=s.addVecToInd(pos,dir)
        if (not newpos in race) and racetrack[newpos]!="#":
            race[newpos]=race[pos]+1
            pos=newpos
            break

cheat_dirs = []
for y in range(-20,21):
    for x in range(-20,21):
        if manhatten_dist((x,y))<21 and manhatten_dist((x,y))>1 and not (abs(x)==1 and abs(y)==1):
            cheat_dirs.append((x,y))

count_task_1 = 0
count_task_2 = 0
for pos,time in race.items():
    for cheat_dir in cheat_dirs:
        if s.outOfBoundsPlusOffset(pos,cheat_dir):
            continue
        cheatpos = s.addVecToInd(pos,cheat_dir)
        if cheatpos not in race:
            continue
        if time+manhatten_dist(cheat_dir)+100<=race[cheatpos]:
            count_task_2+=1
            if (manhatten_dist(cheat_dir)==2):
                count_task_1+=1

print("task1:",count_task_1,"   task2:",count_task_2)
