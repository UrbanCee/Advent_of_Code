import re
with open("inputs/day11_train.txt") as fp:
    connections = {node:{con for con in line.strip().split()} for node,line in re.findall("([a-z]+):([a-z ]+)",fp.read())}

print(connections)