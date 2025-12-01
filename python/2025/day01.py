import re
from itertools import accumulate as acc
with open("inputs/day01.txt") as fp:
    input=[(lr,int(d)) for lr,d in re.findall(r'([LR])([0-9]+)',fp.read())]

print("Task 1:",sum(v%100==0 for v in acc([-d if lr=='L' else d for lr,d in input ],initial=50)))
print("Task 2:",sum(v%100==0 for v in acc([-1 if lr=='L' else 1 for lr,d in input for _ in range(d)],initial=50)))

