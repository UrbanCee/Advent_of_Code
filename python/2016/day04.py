import re
encRoomNamesExpr="([a-z]+)\\-"
idcrcExpr="(\\d+)\\[([a-z]+)\\]"

realRoomIDSum=0
northPoleObjectsID=0
with open("inputs/day04.txt") as fp:
    for line in fp.readlines():
        roomName = "".join([fr for fr in re.findall(encRoomNamesExpr,line)])
        for id,crc in re.findall(idcrcExpr,line):
            charInv={}
            for ch in roomName:
                if ch in charInv:
                    charInv[ch]=charInv[ch]+1
                else:
                    charInv[ch]=1
            sortedInv=sorted([(chr,count) for (chr,count) in charInv.items()],key=lambda t:(t[1],ord('z')-ord(t[0])),reverse=True)
            if "".join([cha for cha,count in sortedInv[:5]])==crc:
                shiftValue=int(id)
                if  "northpoleobject" in "".join([chr(ord('a')+((ord(ch)-ord('a')+shiftValue)%26)) for ch in roomName]):
                    northPoleObjectsID=shiftValue
                realRoomIDSum+=shiftValue


print("Task1: ",realRoomIDSum)
print("Task2: ",northPoleObjectsID)