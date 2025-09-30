import re
from collections import deque

pat1 = re.compile(r'Begin in state ([A-Z])\.Perform a diagnostic checksum after ([0-9]*) steps\.')
pat2 = re.compile(r'In state ([A-Z]):\s*If the current value is 0:[-\s]*Write the value ([01]).[-\s]*Move one slot to the (right|left).[-\s]*Continue with state ([A-Z]).[-\s]*If the current value is 1:[-\s]*Write the value ([01]).[-\s]*Move one slot to the (right|left).[-\s]*Continue with state ([A-Z]).')

with open("inputs/day25.txt") as fp:
    input=fp.read().replace('\r', '').replace('\n', '')
    currentState, steps = [(c,int(s)) for c,s in pat1.findall(input)][0]
    program = {state:((int(val0),dir0,next0),(int(val1),dir1,next1)) for state,val0,dir0,next0,val1,dir1,next1 in pat2.findall(input)}

tape, pos = deque([0]),0

while steps > 0:
    val,dir,currentState=program[currentState][tape[pos]]
    tape[pos]=val
    pos+=1 if dir=='right' else -1
    if pos<0:
        tape.appendleft(0)
        pos=0
    if pos==len(tape):
        tape.append(0)
    steps-=1

print("Task 1:",tape.count(1))

