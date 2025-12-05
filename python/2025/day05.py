import re
with open("inputs/day05.txt") as fp:
    input = fp.readlines()
    ranges = [(int(a),int(b)) for line in input for a,b in re.findall(r"(\d+)\-(\d+)",line)]

print("Task 1:",sum(sum(i>=a and i<=b for a,b in ranges)>0 for i in [int(i) for line in input for i in re.findall(r"^(\d+)\r?\n",line)]))
rangeUnion = []
    