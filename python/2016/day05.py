import hashlib

current_num=0
passwd1=""
passwd2="XXXXXXXX"
passwd2len=0
while len(passwd1)<8 or passwd2len<8:
    md=hashlib.md5()
    encStr=bytes("uqwqemis"+str(current_num),"utf-8")
    md.update(encStr)
    if (md.hexdigest()[0:5]=="00000"):
        if (len(passwd1)<8): passwd1+=md.hexdigest()[5]
        pass2pos=int(md.hexdigest()[5],16)
        if pass2pos>=0 and pass2pos<8 and passwd2[pass2pos]=="X":
            passwd2=passwd2[:pass2pos]+md.hexdigest()[6]+passwd2[pass2pos+1:]
            passwd2len+=1
            print(passwd2)
    current_num+=1
    

print("Task1: ",passwd1)
print("Task2: ",passwd2)
