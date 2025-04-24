input=".^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^"

trapPatterns = ["^..","..^","^^.",".^^"]
    
def createTrapRoom(row,additionalRowCount):
    safecount=row.count(".")
    for i in range(additionalRowCount):
        lastrow="."+row+"."
        row="".join(["^" if lastrow[j:j+3] in trapPatterns else "." for j in range(len(row))])
        safecount+=row.count(".")
    return safecount

print("Task1: ",createTrapRoom(input,39))
print("Task2: ",createTrapRoom(input,399999))
