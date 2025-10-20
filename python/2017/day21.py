import re
from textwrap import wrap
from collections import Counter
import math
re2x2 = re.compile(r"([.#]{2})\/([.#]{2}) => ([.#]{3})\/([.#]{3})\/([.#]{3})")
re3x3 = re.compile(r"([.#]{3})\/([.#]{3})\/([.#]{3}) => ([.#]{4})\/([.#]{4})\/([.#]{4})\/([.#]{4})")
with open("inputs/day21.txt") as fp:
    rules = "".join([s.strip() for s in fp.readlines()])
rules2 = {l1+l2:r1+r2+r3 for l1,l2,r1,r2,r3 in re2x2.findall(rules)}
rules3 = {l1+l2+l3:r1+r2+r3+r4 for l1,l2,l3,r1,r2,r3,r4 in re3x3.findall(rules)}
start = ".#...####"
def printstencil(str,w):
    print("\n".join(wrap(str,width=w)))
def flip2v(str):return str[2:]+str[:2]
def flip2h(str):return str[1]+str[0]+str[3]+str[2]
def rotcw2(str):return str[-2::-2]+str[-1::-2]
def flip3v(str):return str[6:]+str[3:6]+str[:3]
def flip3h(str):return str[2::-1]+str[5:2:-1]+str[:5:-1]
def rotcw3(str):return str[-3::-3]+str[-2::-3]+str[-1::-3]
def test2(str,pattern):
    return str in {pattern,flip2v(pattern),flip2h(pattern),flip2h(flip2v(pattern)),rotcw2(pattern),rotcw2(flip2v(pattern)),rotcw2(flip2h(pattern)),rotcw2(flip2h(flip2v(pattern)))}
def test3(str,pattern):
    return str in {pattern,flip3v(pattern),flip3h(pattern),flip3h(flip3v(pattern)),rotcw3(pattern),rotcw3(flip3v(pattern)),rotcw3(flip3h(pattern)),rotcw3(flip3h(flip3v(pattern)))}
def applyRule(pattern,rule,testfunc):
    for key,value in rule.items():
        if testfunc(pattern,key):
            return value
    return ""
def extract(field,width,size,tileX,tileY):
    return "".join([field[(tileY*size+i)*width+tileX*size:(tileY*size+i)*width+(tileX+1)*size]for i in range(size)])
def combine3x3s(tokenarray):
    size=int(math.sqrt(len(tokenarray)))
    return "".join(["".join([tokenarray[tilex+size*tiley][row*3:(row+1)*3] for tilex in range(size)])  for tiley in range(size) for row in range(3)])
def three2nine(ini3x3):
    interm=applyRule(ini3x3,rules3,test3)
    for i in range(2,4):
        interm=combine3x3s([applyRule(extract(interm,2*i,2,x,y),rules2,test2) for y in range(i) for x in range(i)])
        if i==2:
            interm_count=interm.count("#")
    return (dict(Counter([extract(interm,9,3,x,y) for y in range(3) for x in range(3)])),interm_count)

print("Task 1:",sum([value*three2nine(key)[1] for key,value in three2nine(start)[0].items()]))

fractal = {start:1}
for i in range(6):
    newFractal = dict()
    for key,value in fractal.items():
        newDict = three2nine(key)[0]
        for newkey,newvalue in newDict.items():
            newFractal[newkey]=newFractal.get(newkey,0)+newvalue*value
    fractal=newFractal

print("Task 2:",sum([key.count("#")*value for key,value in fractal.items()]))