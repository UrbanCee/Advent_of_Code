import math

def vAdd(v1 : tuple[int,int],v2 : tuple[int,int]) -> tuple[int,int]:
    return (v1[0]+v2[0],v1[1]+v2[1])
def vSub(v1: tuple[int,int],v2: tuple[int,int]) -> tuple[int,int]:
    return (v1[0]-v2[0],v1[1]-v2[1])
def vMul(v: tuple[int,int],f : int) -> tuple[int,int]:
    return (v[0]*f,v[1]*f) 
def manDist(v: tuple[int,int]) -> int:
    return abs(v[0])+abs(v[1])

def v3Add(v1 : tuple[int,int,int],v2 : tuple[int,int,int]) -> tuple[int,int,int]:
    return (v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2])
def v3Sub(v1 : tuple[int,int,int],v2 : tuple[int,int,int]) -> tuple[int,int,int]:
    return (v1[0]-v2[0],v1[1]-v2[1],v1[2]-v2[2])
def v3Mul(v: tuple[int,int,int],f : int) -> tuple[int,int,int]:
    return (v[0]*f,v[1]*f,v[2]*f) 
def man3Dist(v: tuple[int,int,int]) -> int:
    return abs(v[0])+abs(v[1])+abs(v[2])
def findBase(v: tuple[int,int]):
    return (v[0]//math.gcd(v[0],v[1]),v[1]//math.gcd(v[0],v[1]))


class mySize:
    w,h=0,0
    def __init__(self,w :int,h:int):
        self.w=w
        self.h=h
    def toInd(self,x:int,y:int) -> int:
        return x+y*self.w
    def toIndv(self,v:tuple[int,int]) -> int:
        return self.toInd(v[0],v[1])
    def toVec(self,index:int) -> tuple[int,int]:
        return (index%self.w,index//self.w)
    def outOfBounds(self,x:int,y:int) -> bool:
        return x<0 or x>=self.w or y<0 or y>=self.h
    def outOfBoundsv(self,v:tuple[int,int]) -> bool:
        return self.outOfBounds(v[0],v[1])
    def outOfBoundsPlusOffset(self,index:int,v:tuple[int,int]) -> bool:
        return self.outOfBoundsv(vAdd(self.toVec(index),v))
    def addVecToInd(self,index:int,v:tuple[int,int]) -> int:
        return self.toIndv(vAdd(self.toVec(index),v))
    def print(self,string):
        for i in range(self.h):
            print(string[i*self.w:(i+1)*self.w])
            
dirs8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
dirs4 = [(1,0),(0,1),(-1,0),(0,-1)]

def charInv(line:str,inv={}):
    return {ch:line.count(ch) for ch in line}

