import itertools

boss = (104,8,1)
weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
armours = [(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
rings = [(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]
player = (100,0,0)

def addstats(s1,s2):
    return (s1[0]+s2[0],s1[1]+s2[1],s1[2]+s2[2])

wepDict = {}
for i in range(len(weapons)):
    wepDict["w"+str(i)]=weapons[i]
arDict = {"a":(0,0,0)}
for i in range(len(armours)):
    arDict["a"+str(i)]=armours[i]
ringDict={"r":(0,0,0)}
for i in range(len(rings)):
    ringDict["r"+str(i)]=rings[i]
for i,j in [(i,j) for i in range(len(rings)) for j in range(len(rings)) if i!=j]:
    ringDict["r"+str(i)+"r"+str(j)]=addstats(rings[i],rings[j])
eqCombos = {}
for wk,ak,rk in [(wk,ak,rk) for wk in wepDict.keys() for ak in arDict.keys() for rk in ringDict.keys()]:
    eqCombos[wk+ak+rk]=addstats(wepDict[wk],addstats(arDict[ak],ringDict[rk]))

def fight(p,b):
    php,pd,pa = p
    bhp,bd,ba = b
    while True:
        bhp-=max(1,pd-ba)
        if (bhp<=0): return True
        php-=max(1,bd-pa)
        if (php<=0): return False

mincost,maxcost=1000000,0
bestCombo,worstCombo="",""
for k,v in eqCombos.items():
    if (fight((100,v[1],v[2]),boss)):
        if v[0]<mincost:
            mincost,bestCombo=v[0],k
    else:
        if v[0]>maxcost:
            maxcost,worstCombo=v[0],k

print("Best Combo to still win:",bestCombo,mincost)
print("worst Combo to still lose:",worstCombo,maxcost)
