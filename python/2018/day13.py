from size import *
dirmap = {">":0,"v":1,"<":2,"^":3}
with open("inputs/day13.txt") as fp:
    lines = [line.strip("\n") for line in fp.readlines() if len(line.strip("\n"))>0]
    s,playfield = mySize(len(lines[0]),len(lines)) , "".join(lines)
    carts = sorted([(index,dirmap[playfield[index]],0,True) for index in range(len(playfield)) if playfield[index]in dirmap],key=lambda x:x[0])
    playfield=playfield.replace(">","-").replace("<","-").replace("^","|").replace("v","|")
while len(carts)>1:
    for i,_ in enumerate(carts):
        index,dir,nextturn,alife = carts[i]
        if not alife:
            continue
        index=s.addVecToInd(index,dirs4[dir])
        colliders = [j for j in range(len(carts)) if j!=i and carts[j][3] and index==carts[j][0]]
        if len(colliders)>0:
            print("Colission at:",s.toVec(index), " - Cart",i,"colliding with cart",colliders[0])
            alife=False
            ci,cd,cnt,ca=carts[colliders[0]]
            carts[colliders[0]]=(ci,cd,cnt,False)
        track = playfield[index]
        if (track=="\\"):
            carts[i]=(index,(dir+1 if dir%2==0 else dir+3)%4,nextturn,alife)
        elif (track=="/"):
            carts[i]=(index,(dir+3 if dir%2==0 else dir+1)%4,nextturn,alife)
        elif (track=="+"):
            carts[i]=(index,(dir+3+nextturn)%4,(nextturn+1)%3,alife)
        else:
            carts[i]=(index,dir,nextturn,alife)
    carts=sorted([c for c in carts if c[3]],key=lambda x:x[0])
print("Task 2: ",s.toVec(carts[0][0]))

