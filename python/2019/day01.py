with open("inputs/day01.txt") as fp:
    masses = [int(ms) for ms in fp.readlines()]

def fuel(m):
    if (m<9):
        return 0
    f = m//3-2
    return f+fuel(f)

print("Task1: ",sum([(m//3-2) for m in masses]))
print("Task2: ",sum([fuel(m) for m in masses]))

