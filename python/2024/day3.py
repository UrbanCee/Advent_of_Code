import re

with open("inputs/day3.txt","rt") as fp:
    line=fp.read().replace("\n","")

mulExp = "mul\\((\\d{1,3}),(\\d{1,3})\\)"
sum1, sum2 = 0, 0
for (s1, s2) in re.findall(mulExp,line):
    sum1 += int(s1)*int(s2)
for (s1, s2) in re.findall(mulExp,re.sub("don't\\(\\).*?do\\(\\)","",line)):
    sum2 += int(s1)*int(s2)

print("Task1:",sum1)
print("Task2:",sum2)