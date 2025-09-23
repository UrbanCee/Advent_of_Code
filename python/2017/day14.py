from functools import reduce
from collections import deque 
from size import *

input = "vbqugkhl"
#input = "flqrgnkx"

def knotHash(input):
    numberList, pos, skipSize = list(range(256)),0 ,0
    for i in range(64):
        for length in [ord(ch) for ch in input]+[17, 31, 73, 47, 23]:
            numberList=numberList[length:]+list(reversed(numberList[:length]))
            numberList=numberList[skipSize:]+numberList[:skipSize]
            pos=(pos+length+skipSize)%len(numberList)
            skipSize=(skipSize+1)%len(numberList)
    sparseHash = numberList[-pos:]+numberList[:-pos]
    return "".join(['{:02x}'.format(reduce(lambda x,y:x^y,sublist)) for sublist in [sparseHash[pos:pos+16] for pos in range(0,255,16)]])

playfield=[c for num in [int(knotHash(input+"-"+str(i)),16) for i in range(128)] for c in ["#" if num&(1<<i) > 0 else "." for i in range(128)][::-1] ]
print("Task 1:",playfield.count("#"))

currentRegion, s = 0, mySize(128,128)
while(playfield.count("#")>0):
    currentRegion+=1
    queue = deque([playfield.index("#")])
    while queue:
        currIndx=queue.pop()
        playfield[currIndx]=str(currentRegion)
        for dir in dirs4:
            if not s.outOfBoundsPlusOffset(currIndx,dir) and playfield[s.addVecToInd(currIndx,dir)]=="#":
                queue.append(s.addVecToInd(currIndx,dir))

print("Task 2:",currentRegion)
    