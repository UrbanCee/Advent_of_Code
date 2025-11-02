import re
from itertools import count
counter = count(1)
armyRex = re.compile(r'(\d+) units each with (\d+) hit points (\(.*\))* ?with an attack that does (\d+) (\w+) damage at initiative (\d+)')
wiRex = re.compile(r'(weak|immune)')
dmgTypeRex = re.compile(r'(bludgeoning|slashing|fire|radiation|cold)')
with open("inputs/day24_train.txt") as fp:
    armies = [[(next(counter),units,hp,dmg,dmgType,ini,{dmgType:(2 if wi=="weak" else 0) for types in dmgMult.split(";") for wi in wiRex.findall(types) for dmgType in dmgTypeRex.findall(types)}) for units,hp,dmgMult,dmg,dmgType,ini in armyRex.findall(infstr)] for infstr in fp.read().split("Infection:")]
                #  0      1    2  3     4     5      6     7
def sortByAttackPower(armies):
    return [sorted(army,key = lambda g:g[2]*g[4]+g[6]/1000) for army in armies]

for armyID in range(2):
    for group in sortByAttackPower(armies[armyID]):
        for target in armies[1-armyID]:
            