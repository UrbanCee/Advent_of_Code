import hashlib
def findFirstOf(findToken,current_num=0):
    while True:
        if (hashlib.md5(bytes("yzbqklnj"+str(current_num),"utf-8")).hexdigest()[0:len(findToken)]==findToken):
            return current_num
        current_num+=1
print("Task1: ",findFirstOf("00000"))
print("Task2: ",findFirstOf("000000"))








