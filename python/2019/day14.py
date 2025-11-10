import re
quantRex = re.compile(r'(\d+) ([A-Za-z]+)')
with open("inputs/day14_train1.txt") as fp:
    recipies = {comp:(int(amt),[(int(amt),comp) for amt,comp in quantRex.findall(educts)]) for educts,products in [line.split("=>") for line in fp.readlines() if len(line)>1] for amt,comp in quantRex.findall(products)}

def ceildiv(a, b):
    return -(a // -b)



print("Task 1:")
