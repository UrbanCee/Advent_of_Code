import re
with open("inputs/day12_train.txt") as fp:
    input=fp.read()
    treeArray = list(zip(*[iter([line for line in re.findall(r'([.#]+)',input)])]*3))
    packings = [(int(w),int(h),[int(amnt) for amnt in amnts.strip().split()]) for w,h,amnts in re.findall(r'(\d+)x(\d+):([ \d]+)',input)]
print(treeArray)
print(packings)