def checksum(a,disksize):
    while(len(a)<disksize):
        a+="0"+"".join(["1" if b=="0" else "0" for b in reversed(a)])
    a=a[:disksize]
    while(len(a)%2==0):
        a="".join(["1" if a[i]==a[i+1] else "0" for i in range(0,len(a),2)])
    return a

print("Task1: ",checksum("10011111011011001",272))
print("Task2: ",checksum("10011111011011001",35651584))

