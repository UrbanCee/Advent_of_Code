import re
armyRex = re.compile(r'(\d+) units each with (\d+) hit points (\(.*\))* ?with an attack that does (\d+) (\w+) damage at initiative (\d+)')
wiRex = re.compile(r'(weak|immune)')
dmgTypeRex = re.compile(r'(bludgeoning|slashing|fire|radiation|cold)')
with open("inputs/day24_train.txt") as fp:
    armies = [[(units,hp,dmg,dmgType,ini,{dmgType:(2 if wi=="weak" else 0) for types in dmgMult.split(";") for wi in wiRex.findall(types) for dmgType in dmgTypeRex.findall(types)}) for units,hp,dmgMult,dmg,dmgType,ini in armyRex.findall(infstr)] for infstr in fp.read().split("Infection:")]

print(armies)
