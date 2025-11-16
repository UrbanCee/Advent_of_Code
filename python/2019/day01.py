with open("inputs/day01.txt") as fp:
    masses = [int(ms) for ms in fp.readlines()]

def fuel(m): return 0 if m<9 else m//3-2 + fuel(m//3-2) 

print("Task1: ",sum([(m//3-2) for m in masses]))
print("Task2: ",sum([fuel(m) for m in masses]))

