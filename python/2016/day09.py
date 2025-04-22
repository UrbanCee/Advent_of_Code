import re

with open("inputs/day09.txt") as fp:
    compressedText=fp.read().strip()

reg="\\((\\d+)x(\\d+)\\)"

def decompress(text:str,version: int):
    skippedLength=text.find("(")
    if skippedLength==-1:
        return len(text)
    else:
        length,times = tuple(map(int,re.search(reg,text).groups()))
        markerlength=len(re.search(reg,text).group(0))
        textafter = text[skippedLength+markerlength+length:]
        if (version==1):
            return skippedLength+length*times+decompress(textafter,1)
        else:
            return decompress(textafter,2)+times*decompress(text[skippedLength+markerlength:skippedLength+markerlength+length],2)

print("Task1:",decompress(compressedText,1))
print("Task2:",decompress(compressedText,2))

