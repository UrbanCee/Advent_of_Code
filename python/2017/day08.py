import re
insPat = re.compile(r'([a-z]+) (inc|dec) (\-?[0-9]+) if ([a-z]+) (==|<|>|<=|>=|!=) (\-?[0-9]+)')
with open("inputs/day08.txt") as fp:
    ins=[(reg,cmd,int(value),regchk,comp,int(comValue)) for line in fp.readlines() for reg,cmd,value,regchk,comp,comValue in insPat.findall(line)]

regs = {}
highestValue=0

for reg,cmd,val,regchk,comp,compVal in ins:
    if eval("regs.get(regchk,0)"+comp+"compVal"):
        if (cmd=="inc"):regs[reg]=regs.get(reg,0)+val
        else: regs[reg]=regs.get(reg,0)-val
        highestValue=max(highestValue,regs[reg])

print("Task 1:",max(regs.values()))
print("Task 2:",highestValue)