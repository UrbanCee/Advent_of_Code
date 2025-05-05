def checkvowelcount(string):
    return sum([string.count(ch) for ch in "aeiuo"])>2

def checkdouble(string):
    return sum([string[i]==string[i+1] for i in range(len(string)-1)])>0

def checkbadcombos(string):
    return sum([cmb in string for cmb in ["ab","cd","pq","xy"]])==0

def sparseletter(string):
    return sum([string[i]==string[i+2] for i in range(len(string)-2)])>0

def checkreoccpair(string):
    return sum([string[i:][0:2] in string[i:][2:] for i in range(len(string)-3)])>0

with open("inputs/day05.txt") as fp:
    lines= list(map(str.strip,fp.readlines()))

print("Task1: ",sum([checkvowelcount(line) and checkdouble(line) and checkbadcombos(line) for line in lines]))
print("Task2: ",sum([checkreoccpair(line) and sparseletter(line) for line in lines]))

