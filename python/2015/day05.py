def checkvowelcount(string):
    vowelcount=0
    for ch in "aeiuo":
        vowelcount+=string.count(ch)
    return vowelcount>2

def checkdouble(string):
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            return True
    return False

def checkbadcombos(string):
    for cmb in ["ab","cd","pq","xy"]:
        if cmb in string:
            return False
    return True

def sparseletter(string):
    for i in range(len(string)-2):
        if string[i]==string[i+2]:
            return True
    return False

def checkreoccpair(string):
    if len(string)<4:
        return False
    if string[0:2] in string[2:]:
        return True
    return checkreoccpair(string[1:])


niceCount1 = 0
niceCount2 = 0
with open("inputs/day05.txt") as fp:
    for line in fp.readlines():
        if checkvowelcount(line) and checkdouble(line) and checkbadcombos(line):
            niceCount1+=1
        if checkreoccpair(line) and sparseletter(line):
            niceCount2+=1

print("Task1: Nice count: ",niceCount1)
print("Task2: Nice count: ",niceCount2)

