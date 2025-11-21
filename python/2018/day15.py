from size import *
with open("inputs/day15.txt") as fp:
    input = [line.strip() for line in fp.readlines() if len(line.strip())>1]
    s = mySize(len(input[0]),len(input))
    room = [ c for line in input for c in line]

s.print(room)