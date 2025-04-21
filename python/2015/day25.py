#"row 2947, column 3029"
row = 2947
column = 3029


def calcPos(r,c):
    return sum([x for x in range(r+c)])-r+1


def valueAtPos(r,c):
    currentValue=20151125
    multi=252533
    divis=33554393
    for i in range (calcPos(r,c)-1):
        currentValue=(currentValue*multi)%divis
    return currentValue

print("Task1: ",valueAtPos(row,column))