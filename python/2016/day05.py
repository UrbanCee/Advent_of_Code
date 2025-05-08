import hashlib

current_num=0
passwd1,passwd2="","XXXXXXXX"

while len(passwd1)<8 or "X" in passwd2:
    passw=hashlib.md5(bytes("uqwqemis"+str(current_num),"utf-8")).hexdigest()
    if (passw[0:5]=="00000"):
        if (len(passwd1)<8): passwd1+=passw[5]
        pass2pos=int(passw[5],16)
        if pass2pos>=0 and pass2pos<8 and passwd2[pass2pos]=="X":
            passwd2=passwd2[:pass2pos]+passw[6]+passwd2[pass2pos+1:]
            print("found new digit: ",passwd2)
    current_num+=1
    

print("Task1: ",passwd1)
print("Task2: ",passwd2)
