import re
import numpy as np

rex = "([A-Za-z]+): capacity (-?\\d+), durability (-?\\d+), flavor (-?\\d+), texture (-?\\d+), calories (-?\\d+)"

ingred = []
ingNames = []

with open("inputs/day15.txt") as fp:
    for line in fp.readlines():
        for (name,cap,dur,flav,tex,cal) in re.findall(rex,line):
            ingNames.append(name)
            ingred.append((int(cap),int(dur),int(flav),int(tex),int(cal)))

def calcScore(amts,ing):
    return max(0,np.sum([amts[j]*ing[j] for j in range(4) ]))

maxscore=0
maxCalScore=0

for i1 in range(100):
    for i2 in range(100-i1):
        for i3 in range (100-i1-i2):
            i4=100-i1-i2-i3
            score=1
            for ingInd in range(4):
                score*=max(0,calcScore((i1,i2,i3,i4),(ingred[0][ingInd],ingred[1][ingInd],ingred[2][ingInd],ingred[3][ingInd])))
            if score>maxscore:
                maxscore=score
            if (calcScore((i1,i2,i3,i4),(ingred[0][4],ingred[1][4],ingred[2][4],ingred[3][4]))==500):
                if score > maxCalScore:
                    maxCalScore=score

print(maxscore)            
print(maxCalScore)            