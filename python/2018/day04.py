import re
shiftRex=re.compile(r'Guard #(\d+)')
wakeSleepRex=re.compile(r'\[1518-\d+-\d+ \d+:(\d+)\] (?:falls asleep|wakes up)')

with open("inputs/day04.txt") as fp:
    guardData = sorted(map(str.strip,fp.readlines()))

currentGuard,sleepStart,guardSleepTimes = -1,-1,{}
for d in guardData:
    if len(shiftRex.findall(d))>0:
        currentGuard = int(shiftRex.findall(d)[0])
        sleepStart=-1
        continue
    for m in wakeSleepRex.findall(d):
        if sleepStart==-1:
            sleepStart=int(m)
        else:
            guardSleepTimes[currentGuard]=guardSleepTimes.get(currentGuard,[])+[(sleepStart,int(m))]
            sleepStart=-1

def calcSleepminutes(guardID):
    sleepminutes={}
    for s,e in guardSleepTimes[guardID]:
        for m in range(s,e):
            sleepminutes[m]=sleepminutes.get(m,0)+1
    return sleepminutes

mostSleepGuardID=max(guardSleepTimes,key=lambda x:sum([b-a for a,b in guardSleepTimes[x]]))
longestSleepGuardSM=calcSleepminutes(mostSleepGuardID)
print("Task 1:",max(longestSleepGuardSM,key=longestSleepGuardSM.get)*mostSleepGuardID)
mostSleepMinutesGuardID=max(guardSleepTimes,key=lambda x: max(calcSleepminutes(x).values()))
mostSpleepMinGuardSM=calcSleepminutes(mostSleepMinutesGuardID)
print("Task 2:",max(mostSpleepMinGuardSM,key=mostSpleepMinGuardSM.get)*mostSleepMinutesGuardID)