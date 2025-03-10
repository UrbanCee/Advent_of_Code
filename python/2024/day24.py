import re

inpExr = "([\\da-z]{3}): ([01])"
gateExpr = "([\\da-z]{3}) (XOR|OR|AND) ([\\da-z]{3}) -> ([\\da-z]{3})"

inputs = {}
gates = {}

with open("inputs/day24_training.txt","rt") as fp:
    for line in fp.readlines():
        for (wire,value) in re.findall(inpExr,line):
            print(wire,value)
        for (in1,gate,in2,out) in re.findall(gateExpr,line):
            print(in1,gate,in2,out)
    
