input=".^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^"
trapPatterns = ["^..","..^","^^.",".^^"]
    
def createTrapRoom(row,additionalRowCount,safecount=0):
    for i in range(additionalRowCount+1):
        safecount+=row.count(".")
        row="".join(["^" if ("."+row+".")[j:j+3] in trapPatterns else "." for j in range(len(row))])
    return safecount

print("Task1: ",createTrapRoom(input,39))
print("Task2: ",createTrapRoom(input,399999))
