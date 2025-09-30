import re

with open("inputs/day24.txt") as fp:
    elements = [(int(i),int(j)) for line in fp.readlines() for i,j in re.findall(r'(\d*)/(\d*)',line)]

