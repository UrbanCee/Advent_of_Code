import re
roomExp=re.compile(r'^([a-z\-]+)(\d+)\[([a-z]+)\]')

with open("inputs/day04.txt") as fp:
    rooms = [(name.replace("-",""),int(id),crc) for line in fp.readlines() for name,id,crc in roomExp.findall(line)]

def sortedInvStr(str):
    sortedList=sorted([(str.count(ch),ch) for ch in {ch for ch in str}],key=lambda t:(t[0],ord('z')-ord(t[1])),reverse=True)
    return "".join([sortedList[i][1] for i in range(5) ])

print("Task1: ",sum([id if sortedInvStr(name)==crc else 0 for name,id,crc in rooms]))
print("Task2: ",sum([id if "northpoleobject" in "".join([chr(ord('a')+((ord(ch)-ord('a')+id)%26)) for ch in name]) else 0 for name,id,crc in rooms]))
