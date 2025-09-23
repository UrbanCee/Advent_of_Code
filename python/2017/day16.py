import re
rex = re.compile(r'([sxp])([0-9a-p]+)/?([0-9a-p]*)')
#programs="abcde"
#dance=[(m,p1,p2) for m,p1,p2 in rex.findall("s1,x3/4,pe/b")]
programs="abcdefghijklmnop"
knownPrograms={programs}
with open("inputs/day16.txt") as fp:
    dance=[(m,p1,p2) for m,p1,p2 in rex.findall(fp.read())]

def swap(s,a,b):
    if a==b : return s
    return s[:min(a,b)]+s[max(a,b)]+s[min(a,b)+1:max(a,b)]+s[min(a,b)]+s[max(a,b)+1:]

def singleStep():
    global programs
    for m,p1,p2 in dance:
        if m=="s": programs=programs[-int(p1):]+programs[:-int(p1)]
        elif m=="x": programs=swap(programs,int(p1),int(p2))
        elif m=="p": programs=swap(programs,programs.index(p1),programs.index(p2))

singleStep()
print("Task 1:",programs)
while programs not in knownPrograms:
    knownPrograms.add(programs)
    singleStep()
for i in range(1000000000%len(knownPrograms)):
    singleStep()
print("Task 2:",programs)


