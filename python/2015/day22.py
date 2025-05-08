from copy import deepcopy

#   (name  ,cost,time,dmg ,heal,ar  ,mana)
spells = [
    ("mm"  ,53  ,0   ,4   ,0   ,0   ,0   ),
    ("dr"  ,73  ,0   ,2   ,2   ,0   ,0   ),
    ("sh"  ,113 ,6   ,0   ,0   ,7   ,0   ),
    ("po"  ,173 ,6   ,3   ,0   ,0   ,0   ),
    ("re"  ,229 ,5   ,0   ,0   ,0   ,101 )
]

init_bossHP,bossdmg =  71,10
init_playerHP,init_mana = 50,500

bestresult=100000000

def fight(bossHP,playerHP,mana,bossturn,effects,manaspent,castSpells,loseHP):
    global bestresult
    stillActiveEffects={}
    playerAr=0
    for k,v in effects.items():
        bossHP-=v[3]
        playerHP+=v[4]
        playerAr+=v[5]
        mana+=v[6]
        if v[2]-1>0:
            stillActiveEffects[k]=(v[0],v[1],v[2]-1,v[3],v[4],v[5],v[6])
    if bossHP<=0:
        print(manaspent,castSpells)
        if manaspent<bestresult:
            bestresult=manaspent
        return True
    if bossturn:
        playerHP-=max(1,bossdmg-playerAr)
        if playerHP>0:
            return fight(bossHP,playerHP,mana,False,stillActiveEffects,manaspent,castSpells,loseHP)
    else:
        if loseHP:
            playerHP-=1
            if playerHP<=0:
                return False
        if mana<53:
            return False
        for spell in spells:
            if spell[0] in stillActiveEffects.keys() or spell[1]>mana or manaspent+spell[1]>=bestresult:
                continue
            newEffects = deepcopy(stillActiveEffects)
            newEffects[spell[0]]=spell
            fight(bossHP,playerHP,mana-spell[1],True,newEffects,manaspent+spell[1],castSpells+f"->{spell[0]}",loseHP)

fight(init_bossHP,init_playerHP,init_mana,False,{},0,"",False)
print("Task1: ",bestresult)    
bestresult=100000000
fight(init_bossHP,init_playerHP,init_mana,False,{},0,"",True)
print("Task2:",bestresult)
    
