with open("inputs/day03_train.txt") as fp:
    banks = [[c for c in line.strip()] for line in fp.readlines() if len(line)>1]

print("Task 1:", sum(int(max(bank[:-1])+max(bank[bank.index(max(bank[:-1]))+1:])) for bank in banks))

