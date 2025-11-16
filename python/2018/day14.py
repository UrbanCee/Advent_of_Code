
input,rec,pos=540561,[3,7],(0,1)

def drawCurrent(rec,pos):
    print(["("+str(ri)+")" if i==pos[0] else ("["+str(ri)+"]" if i==pos[1] else ri) for i,ri in enumerate(rec)])

def newRec(rec:list,pos):
    newRec = rec[pos[0]]+rec[pos[1]]
    if newRec>=10: rec.extend([1,newRec%10])
    else: rec.append(newRec)
    return (rec,((pos[0]+1+rec[pos[0]])%len(rec),(pos[1]+1+rec[pos[1]])%len(rec)))
while len(rec)<input+10:
    rec,pos=newRec(rec,pos)
print("Task 1:","".join([str(r) for r in rec[input:input+10]]))

inputarray,rec,pos=[5,4,0,5,6,1],[3,7],(0,1)
while rec[len(rec)-len(inputarray):len(rec)]!=inputarray and rec[len(rec)-1-len(inputarray):len(rec)-1]!=inputarray:
    rec,pos=newRec(rec,pos)
print("Task 2:",len(rec)-len(inputarray) if rec[len(rec)-len(inputarray):len(rec)]==inputarray else len(rec)-len(inputarray)-1)

    


