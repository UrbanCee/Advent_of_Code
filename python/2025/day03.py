with open("inputs/day03.txt") as fp:
    banks = [[c for c in line.strip()] for line in fp.readlines() if len(line)>1]

def calcMax(arr,i):
    return max(arr) if i==0 else max(arr[:-i])+calcMax(arr[arr.index(max(arr[:-i]))+1:],i-1)

print("Task 1:", sum(int("".join(calcMax(bank,1))) for bank in banks))
print("Task 2:", sum(int("".join(calcMax(bank,11))) for bank in banks))

