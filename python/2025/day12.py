import re
with open("inputs/day12.txt") as fp:
    input=fp.read()
    shapes = ["".join(a) for a in list(zip(*[iter([line for line in re.findall(r'([.#]+)',input)])]*3))]
    packings = [(int(w),int(h),[int(amnt) for amnt in amnts.strip().split()]) for w,h,amnts in re.findall(r'(\d+)x(\d+):([ \d]+)',input)]

print("Task 1:",sum(x*y>sum(s.count("#")*amts[i] for i,s in enumerate(shapes)) for x,y,amts in packings))
