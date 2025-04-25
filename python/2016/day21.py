import re
from itertools import permutations

swpPosPat=re.compile(r'swap position (\d+) with position (\d+)')
swpLetPat=re.compile(r'swap letter (\w+) with letter (\w+)')
rotatePat=re.compile(r'rotate (left|right) (\d+) steps*')
rotatePosPat=re.compile(r'rotate based on position of letter (\w+)')
reversePat=re.compile(r'reverse positions (\d+) through (\d+)')
movePat=re.compile(r'move position (\d+) to position (\d+)')


with open("inputs/day21.txt") as fp:
    cmds = list(map(str.strip,fp.readlines()))
    
code = "abcdefgh"
def encrypt(code):
    for cmd in cmds:
        for X,Y in [(min(int(X),int(Y)),max(int(X),int(Y))) for X,Y in swpPosPat.findall(cmd)]:
            code=code[:X]+code[Y]+code[X+1:Y]+code[X]+code[Y+1:]
        for X,Y in [(min(code.find(cx),code.find(cy)),max(code.find(cx),code.find(cy))) for cx,cy in swpLetPat.findall(cmd)]:
            code=code[:X]+code[Y]+code[X+1:Y]+code[X]+code[Y+1:]
        for dir,steps in rotatePat.findall(cmd):
            if dir=="left": code = "".join([code[(i+int(steps))%len(code)] for i in range(len(code))])
            else: code = "".join([code[(i+len(code)-int(steps))%len(code)] for i in range(len(code))])
        for letter in rotatePosPat.findall(cmd):
            steps = code.find(letter)
            if steps>=4: steps+=2
            else: steps+=1
            code="".join([code[(i+len(code)-steps)%len(code)] for i in range(len(code))])
        for X,Y in [(min(int(X),int(Y)),max(int(X),int(Y))) for X,Y in reversePat.findall(cmd)]:
            code=code[:X]+(code[X:Y+1][::-1])+code[Y+1:]
        for X,Y in [(int(X),int(Y)) for X,Y in movePat.findall(cmd)]:
            intCode=code[:X]+code[X+1:]
            code=intCode[:Y]+code[X]+intCode[Y:]
    return code
print("Task1: ",encrypt("abcdefgh"))
for code in ["".join(perm) for perm in permutations("abcdefgh")]:
    if encrypt(code)=="fbgdceah":
        print("Task2: ",code)
        break
        

