import re
shiftRex=re.compile(r'Guard #(\d+)')
wakeSleepRex=re.compile(r'\[1518-(\d+)-(\d+) (\d+):(\d+)\] (falls asleep|wakes up)')

with open("inputs/day04_train.txt") as fp:
    guardData = sorted(map(str.strip,fp.readlines()))

currentGuard,sleepStart,guardSleepTimes = -1,-1,{}
for d in guardData:
    if len(shiftRex.findall(d))>0:
        currentGuard = int(shiftRex.findall(d)[0])
        sleepStart=-1
        continue
    for m,d,h,m,type in wakeSleepRex.findall(d):
        if sleepStart==-1:
            sleepStart=int(m)
        else:
            guardSleepTimes[currentGuard]=guardSleepTimes.get(currentGuard,[])+[(sleepStart,int(m)-1)]
            sleepStart=-1


print(guardSleepTimes)
