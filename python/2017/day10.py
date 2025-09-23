from functools import reduce

def knotHash(input,amount):
    numberList, pos, skipSize = list(range(256)),0 ,0
    for i in range(amount):
        for length in input:
            numberList=numberList[length:]+list(reversed(numberList[:length]))
            numberList=numberList[skipSize:]+numberList[:skipSize]
            pos=(pos+length+skipSize)%len(numberList)
            skipSize=(skipSize+1)%len(numberList)
    return numberList[-pos:]+numberList[:-pos]


with open("inputs/day10.txt") as fp:
    hash1=knotHash([int(num) for num in fp.read().strip().split(",")],1)
print("Task 1:",hash1[0]*hash1[1])

with open("inputs/day10.txt") as fp:
    hash2=knotHash([ord(ch) for ch in fp.read().strip()]+[17, 31, 73, 47, 23],64)
print("Task 2:","".join(['{:02x}'.format(reduce(lambda x,y:x^y,sublist)) for sublist in [hash2[pos:pos+16] for pos in range(0,255,16)]]))
