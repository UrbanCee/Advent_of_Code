import re
insPat = re.compile(r'([a-z]+) (inc|dec) (\-?[0-9]+) if ([a-z]+) (==|<|>|<=|>=|!=) (\-?[0-9]+)')
with open("inputs/day08_train.txt") as fp:
    ins=[(reg,cmd,int(value),regchk,comp,int(comValue)) for line in fp.readlines() for reg,cmd,value,regchk,comp,comValue in insPat.findall(line)]
    
print(ins)