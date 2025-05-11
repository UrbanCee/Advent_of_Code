import re
with open("inputs/day01.txt") as fp:
    nmbrs = [int(num) for line in fp.readlines() for num in re.compile(r'\+?(\-?\d+)').findall(line)]

def find_first(pos=0,visited = {0}):
    while True: 
        for nmbr in nmbrs:
            pos+=nmbr
            if pos in visited: return pos
            visited.add(pos)

print("Task 1:",sum(nmbrs))
print("Task 2:",find_first())