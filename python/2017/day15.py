G=(699,124)
#G=(65,8921)

def match(AB):
    return AB[0]&(1<<16)-1==AB[1]&(1<<16)-1
def nextA(a): return (a*16807)%2147483647
def nextB(b): return (b*48271)%2147483647

def G1():
    g=(G[0],G[1])
    for i in range(40000000):
        g=(nextA(g[0]),nextB(g[1]))
        yield g

print("Task 1:",sum([match(g) for g in G1()]))

def G2():
    a,b=G
    for i in range(5000000):
        a,b = nextA(a),nextB(b)
        while(a&3>0):a=nextA(a)
        while(b&7>0):b=nextB(b)
        yield (a,b)

print("Task 1:",sum([match(g) for g in G2()]))

