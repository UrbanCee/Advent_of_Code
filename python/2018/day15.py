from size import *
from queue import PriorityQueue as pq
with open("inputs/day15_train1.txt") as fp:
    input = [line.strip() for line in fp.readlines() if len(line.strip())>1]
    s = mySize(len(input[0]),len(input))
    room = [ c for line in input for c in line]

hp = {i:200 for i in range(len(room)) if room[i] in {"G","E"}}
initiativeOrder = [i for i in range(len(room)) if room[i] in {"G","E"}]

    