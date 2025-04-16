import re

expr = "\\\\x([0-9a-fA-F]{2})|\\\\\"|\\\\\\\\"

count = 0
countenc = 0
with open("inputs/day08.txt") as fp:
    for line in fp.readlines():
        shortLine = re.sub(expr,"'",line)
        count+=len(line)-(len(shortLine)-2)
        countenc+=line.count("\\")+line.count("\"")+2

print("Task1:",count)
print("Task2:",countenc)

