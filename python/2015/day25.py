#"row 2947, column 3029"
def valueAtPos(r,c,currentValue,multi,divis):
    for i in range (sum([x for x in range(r+c)])-r):
        currentValue=(currentValue*multi)%divis
    return currentValue

print("Task1: ",valueAtPos(2947,3029,20151125,252533,33554393))