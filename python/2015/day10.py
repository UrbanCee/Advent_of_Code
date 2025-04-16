from itertools import groupby

def sizeAfterIterations(string,iterations):
    for i in range(iterations):
        string ="".join([str(len(list(groupList)))+str(char) for char,groupList in groupby(string)])
    return len(string)



print("Task1: ",sizeAfterIterations("3113322113",40))
print("Task2: ",sizeAfterIterations("3113322113",50))



#print(len(look_and_say("3113322113",50)))