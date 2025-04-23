import hashlib

#input = "abc"
input = "ihaygndm"

def hasTriple(s):
    for i in range(len(s)-2):
        if s[i]==s[i+1]:
            if s[i]==s[i+2]:
                return s[i]*5
                
    return ""

def calc(stretch):
    index = 0
    foundTriples = []
    foundKeyIndexes = set()
    while len(foundKeyIndexes)<80:
        hashstring=hashlib.md5(bytes(input+str(index),"utf-8")).hexdigest()
        for i in range(stretch):
            hashstring=hashlib.md5(bytes(hashstring,"utf-8")).hexdigest()
        triple = hasTriple(hashstring)
        if len(triple)>0:
            foundTriples.append((index,triple))
        for indx,tr in foundTriples:
            if indx==index or indx+1000<index:
                continue
            if tr in hashstring:
                foundKeyIndexes.add(indx)
        index+=1
    return sorted(foundKeyIndexes)

print("Task1: ",calc(0)[63])
print("Task1: ",calc(2016)[63])
