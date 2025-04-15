import re
import numpy as nump

wireReg = "^([a-z0-9]+) -> ([a-z]+)"
gateReg = "^([a-z0-9]*) *([A-Z]+) ([a-z0-9]+) -> ([a-z]+)"

wires = {}
gates = [] # tuples with (OP,Dest,IN2,IN1,done)


with open("inputs/day07.txt") as fp:
    for line in fp.readlines():
        for (srcWire,destWire) in re.findall(wireReg,line):
            gates.append(("CP",destWire,srcWire,"")) 
        for (in1,op,in2,out) in re.findall(gateReg,line):
            gates.append((op,out,in2,in1))

def run():
    keepRunning=True
    while(keepRunning):
        keepRunning = False
        for index in range(len(gates)):
            op,out,in2,in1 = gates[index]
            if out in wires:
                continue
            keepRunning=True
            if in1.isnumeric():
                in1n=nump.uint16(in1)
            else:
                if len(in1)>0:
                    if in1 not in wires.keys():
                        continue
                    else:
                        in1n=wires[in1]
            if in2.isnumeric():
                in2n=nump.uint16(in2)
            else:
                if in2 not in wires.keys():
                    continue
                else:
                    in2n=wires[in2]
            if op == "CP":
                wires[out]=in2n
            elif op == "NOT":
                wires[out]= ~in2n
            elif op == "AND":
                wires[out]= in1n & in2n
            elif op == "OR":
                wires[out]= in1n | in2n
            elif op == "LSHIFT":
                wires[out]= in1n << in2n
            elif op == "RSHIFT":
                wires[out]= in1n >> in2n


#    print("-----------wires---------------")
#    for wire,value in wires.items():
#            print(wire,value)
run()
a = wires["a"]
print("Task 1 Wire a=",a)
wires.clear()
wires["b"]=a
run()
a = wires["a"]
print("Task 2 Wire a=",a)







