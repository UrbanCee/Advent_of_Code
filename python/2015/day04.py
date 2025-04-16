import hashlib

found_num=0
current_num=0
while found_num==0:
    md=hashlib.md5()
    encStr=bytes("yzbqklnj"+str(current_num),"utf-8")
    md.update(encStr)
    if (md.hexdigest()[0:6]=="000000"):
        break
    current_num+=1
print(current_num)








