import re
with open("inputs/day06.txt") as fp:
    coords = [(int(x),int(y)) for line in fp.readlines() for x,y in re.compile(r'(\d+), (\d+)').findall(line)]

topLeft = (min([x for x,y in coords]),min([y for x,y in coords]))
bottomRight = (max([x for x,y in coords]),max([y for x,y in coords]))

