with open("inputs/day01.txt") as fp:
    line = fp.readline().strip()

sum=[0,0]
offsets=[1,len(line)//2]
for pos in range(len(line)):
    for task in range(2):
        if line[pos]==line[(pos+offsets[task])%len(line)]:
            sum[task]+=int(line[pos])
print("Task 1:",sum[0])
print("Task 2:",sum[1])
    

    