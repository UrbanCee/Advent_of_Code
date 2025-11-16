from functools import reduce
teststr="19617804207202209144916044189917"
pattern=[0,1,0,-1]
with open("inputs/day_16.txt") as fp:
    input = [int(c) for c in fp.read().strip()]
    #input = [int(c) for c in teststr]

def step(input):
    return [abs(sum(input[j]*pattern[((j+1)//(i+1))%len(pattern)] for j in range(len(input))))%10 for i in range(len(input))]
def printArray(input):
    return "".join([str(i) for i in step(input)])

print("Task 1:",printArray(reduce(lambda c,_: step(c) , range(99), input))[0:8])