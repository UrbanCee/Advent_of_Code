import re

inpExr = "([\\da-z]{3}): ([01])"
gateExpr = "([\\da-z]{3}) (XOR|OR|AND) ([\\da-z]{3}) -> ([\\da-z]{3})"

wires = {}
gates = []

def isactive(w):
    return wires.get(w,-1)>=0

class Gate:
    in1,in2,gtype,out,name,unit,swapped = "","","","","",-1,False
    def __init__(self,in1,in2,gtype,out):
        self.in1=in1
        self.in2=in2
        self.gtype=gtype
        self.out=out
    def __str__(self):
            if (self.swapped):
                return self.name+" in unit "+str(self.unit)+": "+self.in1+": "+str(wires.get(self.in1,-1))+" "+self.gtype+" "+self.in2+": "+str(wires.get(self.in2,-1))+" -> "+self.out+": "+str(wires.get(self.out,-1))+" swapped!!"
            return self.name+" in unit "+str(self.unit)+": "+self.in1+": "+str(wires.get(self.in1,-1))+" "+self.gtype+" "+self.in2+": "+str(wires.get(self.in2,-1))+" -> "+self.out+": "+str(wires.get(self.out,-1))
    def update(self):
        if (isactive(self.out)):
            return True
        if (isactive(self.in1) and isactive(self.in2)):
            if (self.gtype=="AND"):
                wires[self.out]=wires[self.in1] & wires[self.in2]
            elif (self.gtype=="OR"):
                wires[self.out]=wires[self.in1] | wires[self.in2]
            else:
                wires[self.out]=wires[self.in1] ^ wires[self.in2]
            return True
        return False


with open("inputs/day24_reini.txt","rt") as fp:
    for line in fp.readlines():
        for (wire,value) in re.findall(inpExr,line):
            wires[wire]=int(value)
        for (in1,gate,in2,out) in re.findall(gateExpr,line):
            gates.append(Gate(in1,in2,gate,out))
wires2=wires.copy()

while not all(list(map(Gate.update,gates))):
    pass

result = 0
for i in range(64):
    result+=wires.get(f"z{i:02}",0)*(2**i)
print("task1:",result)

print("OR#: ",sum(x.gtype=="OR" for x in gates))
print("AND#: ",sum(x.gtype=="AND" for x in gates))
print("XOR#: ",sum(x.gtype=="XOR" for x in gates))

wireExpr="[xyz](\\d\\d)"
def getUnit(wire : str):
    return int(re.findall(wireExpr,wire)[0])

def gatesByInWire(wire : str):
    return [g for g in gates if g.in1==wire or g.in2==wire]
def gatesByOutWire(wire : str):
    return [g for g in gates if g.out==wire]
def gateByUnitAndName(unit : int, name : str):
    return next((g for g in gates if g.unit==unit and g.name==name))
def existsUnitAndName(unit : int, name : str):
    return len([g for g in gates if g.unit==unit and g.name==name])>0

#naming inxors and inands
swappedwires=[]
for gate in gates:
    if gate.gtype=="XOR" and ((gate.in1[0]=="x" and gate.in2[0]=="y")or(gate.in1[0]=="y" and gate.in2[0]=="x")):
        gate.name="inxor"
        gate.unit=getUnit(gate.in1)
    if gate.gtype=="AND" and ((gate.in1[0]=="x" and gate.in2[0]=="y")or(gate.in1[0]=="y" and gate.in2[0]=="x")):
        gate.name="inand"
        gate.unit=getUnit(gate.in1)
#naming testing outxors
for gate in gates:
    if gate.gtype=="XOR" and gate.name=="":
        gate.name="outxor"
        if (gate.out[0]=="z"):
            gate.unit=getUnit(gate.out)
        else:
            gate.swapped=True
            swappedwires.append(gate.out)
            print(gate)
    else:
        if (gate.gtype=="AND" and gate.name==""):
            gate.name="carryand"
        elif(gate.gtype=="OR" and gate.name==""):
            gate.name="carryor"
        if gate.out[0]=="z" and gate.out!="z00" and gate.out!="z45":
            swappedwires.append(gate.out)
            gate.swapped=True
            print(gate)

#check inxor->outcor per unit
for unit in range (1,45):
    inxor=gateByUnitAndName(unit,"inxor")
    if (existsUnitAndName(unit,"outxor")):
        outxor=gateByUnitAndName(unit,"outxor")
        if (outxor.in1!=inxor.out and outxor.in2!=inxor.out):
            inxor.swapped=True
            swappedwires.append(inxor.out)
            print(inxor)
            print("Failed wire connected to:")
            for g in gatesByInWire(inxor.out):
                print(g)
    else:
        print(inxor)

#check type: inand must be connected to carryor
for gate in gates:
    if gate.name=="inand":
        connectedGates = gatesByInWire(gate.out)
        if (gate.unit==0):
            continue
        if (len(connectedGates)>0 and (len(connectedGates)>1 or gatesByInWire(gate.out)[0].name!="carryor")):
            gate.swapped=True
            swappedwires.append(gate.out)
            print(gate)
            print("Failed wire connected to")
            for g in gatesByInWire(gate.out):
                print(g)


print(",".join(sorted(swappedwires)))
