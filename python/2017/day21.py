import re
from textwrap import wrap
re2x2 = re.compile(r"([.#]{2})\/([.#]{2}) => ([.#]{3})\/([.#]{3})\/([.#]{3})")
re3x3 = re.compile(r"([.#]{3})\/([.#]{3})\/([.#]{3}) => ([.#]{4})\/([.#]{4})\/([.#]{4})\/([.#]{4})")
with open("inputs/day21.txt") as fp:
    rules = "".join([s.strip() for s in fp.readlines()])

rules2 = {l1+l2:r1+r2+r3 for l1,l2,r1,r2,r3 in re2x2.findall(rules)}
rules3 = {l1+l2+l3:r1+r2+r3+r4 for l1,l2,l3,r1,r2,r3,r4 in re3x3.findall(rules)}

test3s = "#....#..."
test2s = "#..."
def printstencil(str,w):
    print("\n".join(wrap(str,width=w)))
def flip2v(str):return str[2:]+str[:2]
def flip2h(str):return str[1]+str[0]+str[3]+str[2]
def flip3v(str):return str[6:]+str[3:6]+str[:3]
def flip3h(str):return str[2::-1]+str[5:2:-1]+str[:5:-1]
def flipdiag(str):return str[8]+str[5]+str[2]+str[1]+str[4]+str[7]+str[6]+str[3]+str[0]

def test2(str,pattern):
    return str in {pattern,flip2v(pattern),flip2h(pattern),flip2h(flip2v(pattern))}
def test3(str,pattern):
    return str in {pattern,flip3v(pattern),flip3h(pattern),flip3h(flip2v(pattern)),flipdiag(pattern),flipdiag(flip3v(pattern)),flipdiag(flip3h(pattern)),flipdiag(flip3h(flip3v(pattern)))}



for test in {test3s,flip3v(test3s),flip3h(test3s),flip3h(flip3v(test3s)),flipdiag(test3s),flipdiag(flip3v(test3s)),flipdiag(flip3h(test3s)),flipdiag(flip3h(flip3v(test3s)))}:
    printstencil(test,3)
    print()

#3x3->4x4->6x6->9x9


