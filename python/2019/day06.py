import re
with open("inputs/day06.txt") as fp:
    orbits = {b:a for a,b in re.findall(r'([A-Za-z0-9]+)\)([A-Za-z0-9]+)',fp.read())}

def orbitHierarchy(body):
    if body not in orbits: return {body}
    return orbitHierarchy(orbits[body])|{body}

print("Task 1:",sum([len(orbitHierarchy(b))-1 for b in orbits.keys()]))
print("Task 2:",len(orbitHierarchy("SAN")^orbitHierarchy("YOU"))-2)
